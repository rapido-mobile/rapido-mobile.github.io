# Input and Display Types
## TOC
 * [Introduction to Rapido](./introduction.md)
 * [1: Make a complete app with a few lines of code](./flutter_app_in_few_lines.md)
 * [2: Brand and light customization](./customize_flutter_app.md)
 * 3: Overview of Input and Display Types
 * [4: Providing your own widgets](./custom_flutter_widgets.md)
 * [5: Adding maps and location](./flutter_maps_and_location.md)
 * [6: Adding images](./flutter_images.md)
 * [7: Document and DocumentList](./rapido_documents.md)
 * [Full Code Example](./main.md)

This is part 3 of the getting started with Rapido tutorial. If you haven't looked through the previous parts, you might want to at least go back and skim those so this part makes sense.

This section is an overview of all of the supported input and display types in Rapido.

When you define a field in a Document or DocumentList, Rapido infers a lot from the way the you name the field. It looks at the end of the field name, and guesses what type is desired from that name. 

## Summary
All the available inferred types are summarized in the table below.  

| Field Name Ends In  | Inferred Dart Type | Default Input Type | Display Type | Field Options |
| ------------- | ------------- | ------------- | ------------- | | ------------- |
| ? | bool | Checkbox | Checkbox | none |
| amount | double | TextInput with numbered keyboard | Text | AmountFieldOptions |
| count | int | TextInput with numbered keyboard, only accepts digits | Text | IntegerPickerFieldOptions |
| date | DateTime | TextInput with date picker | Text | DateTimeFieldOptions |
| datetime | DateTime | TextInput with date picker | Text | DateTimeFieldOptions |
| image | String | Image picker, on device and URLs supported | Image | none |
| latlong | Map<String, double> | Map picker | Map | none |
| text | String | Multi-line input | String | none |

## Defining Your Fields
There are two ways to tell your DocumentList what fields the Documents it contain will have, explicitly and implicitly.

### Explicit Definition
You explicitly define your fields in a DocumentList using the lables property. This is a map of strings to strings (i.e. Map<String, String>). The keys (the first string) are the labels that you want to show in the UI, and the values are the field names that you want to use internally. This is useful because you can use any term that makes sense to users in the UI, and use whatever field name makes sense to users internally.

```dart
    final DocumentList documentList = DocumentList(
    "tasker",
        labels: {
            "Checked": "?",
            "Decimal Number": "amount",
            "Intenger Number": "count",
            "Start Date": "date",
            "End Time": "datetime",
            "Picture": "image",
            "Map Location": "latlong",
            "Long Description": "text",
        },
    );
```

If we use this DocumentList in a DocumentListScaffold or DocumentListView, Rapido will then create the specific UI for each field.

You can see that it renders the UI labels that you defined in the label keys, but knows the appropriate input types based on the values:  
[input form](../assets/typed-form-1.png)  
[input form](../assets/typed-form-2.png)  

Rapido adds the appropriate input UI for differet types. Notice that the first field is a checkbox, for instance. Further examples include numbers keyboard:  
[input form](../assets/integer-input.png) 

Dates and datetime get the date and time pickers:  
[input form](../assets/datetime-input.png)

Images supports the camera, gallery, and URL inputs:  
[input form](../assets/camera-input.png)

Multiline text field is created:  
[input form](../assets/multiline-input.png)

### Implicit Definition
Defining a lables property is useful, but not required. If the labels property is not defined, then Rapido will create it automatically from the first Document in the DocumentList. When inferring types, Rapdio ignores capitalization. 

In the following code, instead of using labels, the code adds a Document with appropriately named fields:

```dart
 final DocumentList documentList = DocumentList(
    "tasker",
    initialDocuments: [
      Document(initialValues: {
        "Completed?": false,
        "Amount": 0,
        "Count": 0,
        "Date": null,
        "Place LatLong": null,
        "Image": null,
        "text": "this can be long if desiered"
      }),
    ],
  );
```

The Document is added to the list as per normal.
[empty document](../assets/empty-document.png)

Now the DocumentListScaffold uses the field names to create an appropriate DocumentForm:  
[input form](../assets/typed-form-3.png) 

## Field Options

