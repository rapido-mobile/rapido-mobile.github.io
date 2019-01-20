import 'package:flutter/material.dart';
import 'package:rapido/rapido.dart';

void main() => runApp(Tasker());

class Tasker extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Tasker',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: TaskerHomePage(),
    );
  }
}

class TaskerHomePage extends StatefulWidget {
  TaskerHomePage({Key key}) : super(key: key);

  @override
  _TaskerHomePageState createState() => _TaskerHomePageState();
}

class _TaskerHomePageState extends State<TaskerHomePage> {
  DocumentList documentList = DocumentList("Tasker", labels: {
    "Task": "title",
    "Date": "date",
    "Priority": "pri count",
    "Note": "subtitle",
    "Map Location": "latlong"
  });

  @override
  @override
  Widget build(BuildContext context) {
    return DocumentListScaffold(
      documentList,
      additionalActions: <Widget>[
        IconButton(icon: Icon(Icons.map), onPressed: navigateToMap),
      ],
      decoration: BoxDecoration(
        image: DecorationImage(
          image: AssetImage("assets/background.jpg"),
          colorFilter: ColorFilter.mode(
              Colors.white.withOpacity(0.05), BlendMode.dstATop),
        ),
      ),
      emptyListWidget: Center(
        child: Text("Click the add button to create your first task"),
      ),
      customItemBuilder: customItemBuilder,
    );
  }

  void navigateToMap() {
    Navigator.push(context, MaterialPageRoute(builder: (BuildContext context) {
      return DocumentListMapView(documentList);
    }));
  }

  Color getCardColor(Document doc) {
    int priority = doc["pri count"];
    if (priority < 3) return Colors.red;
    if (priority < 6) return Colors.yellow;
    return Colors.green;
  }

  Widget customItemBuilder(int index, Document doc, BuildContext context) {
    TextTheme textTheme = Theme.of(context).textTheme;

    return Card(
      color: getCardColor(doc),
      child: Column(
        children: <Widget>[
          Text(
            doc["title"],
            style: textTheme.display1,
          ),
          Text(
            doc["date"],
            style: textTheme.headline,
          ),
          Text(
            doc["subtitle"],
            style: textTheme.subhead,
          ),
          TypedDisplayField(
            fieldName: "latlong",
            document: doc,
            boxSize: 200.00,
          ),
          DocumentActionsButton(documentList, index: index),
        ],
      ),
    );
  }
}
