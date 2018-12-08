# Tutorial Overview
This is part 4 of the getting started with Rapido tutorial. If you haven't looked through [part 1](get_started_part_1.md), [part 2](get_started_part_2.md), or [part 3](get_started_part_3.md) you might want to at least go back and skim those so this part makes sense.

In this section we will add a map location to each task, and display a map with each entry.

## Starting Point
At this point we have a fully functional task application that has some of our branding and we've supplied some custom widgets for the individual task items. 
![with actions](../assets/custom-builder-5.png)

## Adding Your API Key
Currently, Rapido supports Google Maps by wrapping and simplifying the Google Maps Flutter Plugin. In order to use the location and mapping functionality, you will need to supply your own API key. This involves signing up for an API key from Google, and then adding the key to your AndroidManifest.xml file and your AppleDelegate.m file.

See the (Google Maps Flutter Plugin)[https://pub.dartlang.org/packages/google_maps_flutter#-readme-tab-] for the detailed instructions. 

## Adding a Map Point Field
In [part 1](get_started_part_1.md) we defined the labels and by extension the fields, that we expect to include in the UI for Document. We will revisit that by adding a "map-point" field to each Document:
```
  DocumentList documentList = DocumentList("Tasker", labels: {
    "Task": "title",
    "Date": "date",
    "Priority": "pri count",
    "Note": "note",
    "Map Location" : "map_point"
  });
```
Like "date" and "count", "map_point" has semantic meaning in Rapido. It means that you want to store a point on a Map. (As an aside, there are other field names with semantic, such as "title," which you will see in a bit.)

## Picker UI
After closing the app, and restarting it, if we go through the UI and choose the edit button for a task, you will see that a new field is exposed, named "Map Location." This is expected because that is what we named it in the labels property. However, if you look closely, notice that there is a map icon button in the field:  
![form with location](../assets/form-with-location.png)

And if we click on that button, it brings up a picker with a map. The user can move the map around and click the floating check mark button to choose a location:  
![location picker](../assets/location-picker.png)

And you can see that the location is added to the form:  
![form with complete location](../assets/form-with-complete-location.png)

## Add the Map to the App

