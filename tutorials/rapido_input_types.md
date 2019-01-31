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
| amount | double | TextInput with numbered keyboard | Text | AmountFieldOptions |
| count | int | TextInput with numbered keyboard, only accepts digits | Text | IntegerPickerFieldOptions |
| date | DateTime | TextInput with date picker | Text | DateTimeFieldOptions |
| datetime | DateTime | TextInput with date picker | Text | DateTimeFieldOptions |
| image | String | Image picker, on device and URLs supported | Image | none |
| latlong | Map<String, double> | Map picker | Map | none |
| text | String | Multi-line input | String | none |
