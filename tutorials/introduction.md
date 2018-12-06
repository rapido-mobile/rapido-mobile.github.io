# Introduction to Rapido
Rapido is an open source libraruy that intends to make cross platform development easy and fun. We do this by taking a document-centric approach to development, and by following Rapid Application Development (RAD) principles whenever possible.

Skip this page and head to the [tutorial](get_started_part_1.md) if you just want to get to the code. 

## What do you mean by "document-centric?"
Many, if not most, applications are centered around a collection of data, whether entered by the the user, or from a central source, often, but not always, on the Internet somehwere. Applications are designed to allow users to create, retrieve, update, and delete this data, or perform some subset of these actions. In a document centric view, each "entity" that the user can perform these actions on, along with the properties of those  is considered a "document."

Take, for example, an application that allows users to collaborate on listing good places to eat in a city for people who cannot eat gluten. Each document would be a restaurant, and it would have certain properties such as address, ratings, an image etc...

In code, each document is represented as a Map with each property having a string for the key, and some other data type for the value. This would be called a dictionary in Python, or an Object in Javascript.

## What is RAD?
Rapid Application Development means that, as a developer, you should get a lot of functionality for not very much work. However, this should not come at the expense of power and flexibility. RAD means that you should only be spending your time as sa developer focused on the parts of your application that are unique.

## What does Rapido do for you?
With Rapido, all you need to do is define the kind of documents that you want in a very easy way, and rapido will provide all of the UI that your users need to interact with those documents at run time. 

This will make a lot more sense if you look at the code, so head over to the [tutorial](get_started_part_1.md).
