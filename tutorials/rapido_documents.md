# Working directly with Document and DocumentList
## TOC
 * [Introduction to Rapido](./introduction.md)
 * [1: Make a complete app with a few lines of code](./flutter_app_in_few_lines.md)
 * [2: Brand and light customization](./customize_flutter_app.md)
 * [3: Providing your own widgets](./custom_flutter_widgets.md)
 * [4: Adding maps and location](./flutter_maps_and_location.md)
 * 6: Document and DocumentList
 * [Full Code Example](./main.md)

In this part of the tutorial, we will take a look at using [Document](https://pub.dartlang.org/documentation/rapido/latest/documents/Document-class.html) and [DocumentList](https://pub.dartlang.org/documentation/rapido/latest/documents/DocumentList-class.html). So far in the example application in the tutorial, the user has been creating, editing, and deleting Documents with the UI that is automatically provided by Rapido for that purpose. In this part of the tutorial, we will be working with JSON we receive from a web service. 

![rick and morty](../assets/c137.png)

## Working with JSON
### Web API
The web service api in this example is the strangley alluring [Rick and Morty API](https://rickandmortyapi.com/). It supports searching for characters, locations, and episodes, but this example will only use characters. It does not require an API key, so it makes the example easier. Also, I friggin' love Rick and Morty.

### Get JSON from the Web Service
There is a lot of boiler plate involved in retrieving JSON from the web and converting it to an object that Flutter can use. I wrote some simple, but not very robust code, that will return a Dart object that the app can use (assuming everything works, which is a terrible assumption to make).

```dart
import 'package:http/http.dart' as http;
import 'dart:convert';

Future<Map> getAndDecodeRemoteJSon(url, {Map<String, String> headers}) async {

  // create the http client
  http.Client client = http.Client();

  // create an untyped Map
  // if the JSON actually returns a list, this will blow up!
  Map object = {};

  // fetch the content from the url
  await client.get(url, headers: headers).then((http.Response response) async {

    // make the conversion and return the result
    await _decodeJson(response.body).then((result) {
      object = result;
    });
  }).whenComplete(client.close); //clean up

  return object;
}

// decode the json
Future _decodeJson(jsonBody) async {
  Map decoded = json.decode(jsonBody);
  return decoded;
}
```
None of this is particularly specific to Rapido so far.

## SearchBar
There are different ways to create a search interface. I opted to grab [the SearchBar package fromo pub](https://pub.dartlang.org/packages/flutter_search_bar). This creates a search bar in the title bar of the app.

## Using the Decoded JSON
First, do some simple string formatting to create the URL for fetching the data:
```dart
    String url = "https://rickandmortyapi.com/api/character/?name=$value";
```
Then, we can use our get and decode code 

```dart
 getAndDecodeRemoteJSon(url).then((Map map) {
  /* do something with map */  
 }
```
This is where we finally get to the heart of the matter. At this point we will have a Map passed in. So now we have to figure out how to parse that Map. The easiest way to do that is to look at the actual json that gets returned. For our purposes, this is easy enough to do [in a web browser](https://rickandmortyapi.com/api/character/?name=pencil), but here is the Json for a search:

```json
{"info":{"count":1,"pages":1,"next":"","prev":""},"results":[{"id":259,"name":"Pencilvester","status":"Dead","species":"Alien","type":"Parasite, Pencil","gender":"Male","origin":{"name":"unknown","url":""},"location":{"name":"Earth (Replacement Dimension)","url":"https://rickandmortyapi.com/api/location/20"},"image":"https://rickandmortyapi.com/api/character/avatar/259.jpeg","episode":["https://rickandmortyapi.com/api/episode/15"],"url":"https://rickandmortyapi.com/api/character/259","created":"2017-12-31T13:33:48.488Z"}]}
```
As is typical, there is no formatting because the Json is intented for computer programs, not humans. In any case, we can see that there is Map in the form of Map<String, dynamic>. We want the results, which is a List. So we can extract that to work on it:

```dart
      List<dynamic> resultList = map["results"];
```
The we can iterate through the results:

```dart
      resultList.forEach((dynamic item) {
        /* do something with each result */
      });
```

## Creating Documents
Finally, we are ready to create a [Document](https://pub.dartlang.org/documentation/rapido/latest/documents/Document-class.html) with each search result. Note that it is typical to write some very specific code that parse out the API result, and make it work the way we want. In this example, we have to pull out "location" which you can see is actually another map, and then pull out the name of the location, which is the only part we care about:

```dart
  Document _docFromSearchResultsMap(Map<String, dynamic> map) {
    // extract the location, which is another map
    Map<String, dynamic> locOb = map["location"];

    // extract the name of the location (or leave it as null)
    String location;
    if (locOb != null) {
      location = locOb["name"];
    }
    // Create the Document with the desired values
    return Document(
      initialValues: {
        "name": map["name"],
        "Status": map["status"],
        "Species": map["species"],
        "Gender": map["gender"],
        "image": map["image"],
        "Origin": map["origin"],
        "Last Location": location,
      },
    );
  }
```

Each time we create a [Document](https://pub.dartlang.org/documentation/rapido/latest/documents/Document-class.html), the search result is automatically saved on the user's device. This is great because if they come back to the app after closing it, their results will still be there.

This also means that you can use the search results anywhere in your app by either passing along the [DocumentList](https://pub.dartlang.org/documentation/rapido/latest/documents/DocumentList-class.html), or, you can create a new instance of the [DocumentList](https://pub.dartlang.org/documentation/rapido/latest/documents/DocumentList-class.html) with the same documentType, and it will read the results from disk. This can dramatically simplify your code base.

## Creating the List
Because the [Document](https://pub.dartlang.org/documentation/rapido/latest/documents/Document-class.html)s fit so naturally fit into a List, we will use a [DocumentList](https://pub.dartlang.org/documentation/rapido/latest/documents/DocumentList-class.html) to organize them.

Create a [DocumentList](https://pub.dartlang.org/documentation/rapido/latest/documents/DocumentList-class.html) along with a documentType string to keep track of the results.
```dart
  [DocumentList](https://pub.dartlang.org/documentation/rapido/latest/documents/DocumentList-class.html) _documentList = DocumentList("c137Results");
```

Now when we iterate through the results, we can add each [Document](https://pub.dartlang.org/documentation/rapido/latest/documents/Document-class.html) to the [DocumentList]([Document](https://pub.dartlang.org/documentation/rapido/latest/documents/DocumentList-class.html)).

```dart
        resultList.forEach((dynamic item) {
          _documentList.add(_docFromSearchResultsMap(item));
        });
```

## Clearing the Results
If the user does another search, we don't want the old results hanging around. Because [DocumentList](https://pub.dartlang.org/documentation/rapido/latest/documents/DocumentList-class.html) is just a List with super powers, it is easy to clean up:

```dart
    _documentList.clear();
```

Note that this will delete all of the [Document](https://pub.dartlang.org/documentation/rapido/latest/documents/Document-class.html)s in the [DocumentList](https://pub.dartlang.org/documentation/rapido/latest/documents/DocumentList-class.html) from the user's device, which is what we want.

## Displaying the Results
Now that you have a [DocumentList](https://pub.dartlang.org/documentation/rapido/latest/documents/DocumentList-class.html) filled with [Document](https://pub.dartlang.org/documentation/rapido/latest/documents/Document-class.html)s, you can focus on displaying the results as you wish. You can see how I created the [Charcter Card](https://github.com/rapido-mobile/c137/blob/master/lib/character_card.dart) for an example, but I bet you can do better.

# Summary
This section covered decoding JSON and using [Document](https://pub.dartlang.org/documentation/rapido/latest/documents/Document-class.html) and [DocumentList](https://pub.dartlang.org/documentation/rapido/latest/documents/DocumentList-class.html) and easily present them.

Checkout [the full example](https://github.com/rapido-mobile/c137) on Github.

There is also [a video on the Youtube Channel](https://www.youtube.com/watch?v=Lb1J992L-gc) that uses the same sample app to show some tips and tricks for [enhancing the Ux with your DocumentListView](https://www.youtube.com/watch?v=Lb1J992L-gc).