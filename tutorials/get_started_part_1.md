# Tutorial Overview
Maybe you read the (introduction to Rapido)[introduction.md], or maybe you didn't. Either ways is fine, this is where we get to code.

## Pre Reqs
This tutorial assumes that you know what Flutter is, and what Dart the programming language is, but it does not assume that you particularly familar with either. You should probably budget an hour to get the pre reqs set up. Once set up, you shouldn't have any issues.

If you have Flutter running, skip to [creating the project](##create-the-project).

### Flutter Itself
Obviously yuou will need to have Flutter installed. Head over to the [install page](https://flutter.io/docs/get-started/install) and follow directions for your opertaing system. 

### An IDE
While you have a choice of IDEs, I strongly prefer Visual [Studio Code](https://code.visualstudio.com/docs/setup/setup-overview) with the Dart and Flutter extensions installed. Though it is useful to have Android Studio installed for setting up emulators.

### Emulators
Emulators are used for the the run/debug cycle. It is much easier to test your code while you are developing. If you followed the instructions for installing Flutter, than you probably already set up an emulator.

## Create the Project
### Create the Code
We are going to create a task list application, named Tasker. So, first thing is to use your command line to create the Tasker project, like this:

```
$ flutter create tasker
```

Depending on your platform and other factors, you will see some output like this:

```
Creating project tasker...
  tasker/ios/Runner.xcworkspace/contents.xcworkspacedata (created)
  tasker/ios/Runner/Info.plist (created)
  tasker/ios/Runner/Assets.xcassets/LaunchImage.imageset/LaunchImage@2x.png (created)
  tasker/ios/Runner/Assets.xcassets/LaunchImage.imageset/LaunchImage@3x.png (created)
  tasker/ios/Runner/Assets.xcassets/LaunchImage.imageset/README.md (created)
  tasker/ios/Runner/Assets.xcassets/LaunchImage.imageset/Contents.json (created)
  tasker/ios/Runner/Assets.xcassets/LaunchImage.imageset/LaunchImage.png (created)
  tasker/ios/Runner/Assets.xcassets/AppIcon.appiconset/Icon-App-76x76@2x.png (created)
  tasker/ios/Runner/Assets.xcassets/AppIcon.appiconset/Icon-App-29x29@1x.png (created)
  tasker/ios/Runner/Assets.xcassets/AppIcon.appiconset/Icon-App-40x40@1x.png (created)
  tasker/ios/Runner/Assets.xcassets/AppIcon.appiconset/Icon-App-20x20@1x.png (created)
  tasker/ios/Runner/Assets.xcassets/AppIcon.appiconset/Icon-App-1024x1024@1x.png (created)
  tasker/ios/Runner/Assets.xcassets/AppIcon.appiconset/Icon-App-83.5x83.5@2x.png (created)
  tasker/ios/Runner/Assets.xcassets/AppIcon.appiconset/Icon-App-20x20@3x.png (created)
  tasker/ios/Runner/Assets.xcassets/AppIcon.appiconset/Contents.json (created)
  tasker/ios/Runner/Assets.xcassets/AppIcon.appiconset/Icon-App-20x20@2x.png (created)
  tasker/ios/Runner/Assets.xcassets/AppIcon.appiconset/Icon-App-29x29@3x.png (created)
  tasker/ios/Runner/Assets.xcassets/AppIcon.appiconset/Icon-App-40x40@2x.png (created)
  tasker/ios/Runner/Assets.xcassets/AppIcon.appiconset/Icon-App-60x60@3x.png (created)
  tasker/ios/Runner/Assets.xcassets/AppIcon.appiconset/Icon-App-60x60@2x.png (created)
  tasker/ios/Runner/Assets.xcassets/AppIcon.appiconset/Icon-App-76x76@1x.png (created)
  tasker/ios/Runner/Assets.xcassets/AppIcon.appiconset/Icon-App-40x40@3x.png (created)
  tasker/ios/Runner/Assets.xcassets/AppIcon.appiconset/Icon-App-29x29@2x.png (created)
  tasker/ios/Runner/Base.lproj/LaunchScreen.storyboard (created)
  tasker/ios/Runner/Base.lproj/Main.storyboard (created)
  tasker/ios/Runner.xcodeproj/project.xcworkspace/contents.xcworkspacedata (created)
  tasker/ios/Runner.xcodeproj/xcshareddata/xcschemes/Runner.xcscheme (created)
  tasker/ios/Flutter/Debug.xcconfig (created)
  tasker/ios/Flutter/Release.xcconfig (created)
  tasker/ios/Flutter/AppFrameworkInfo.plist (created)
  tasker/test/widget_test.dart (created)
  tasker/tasker.iml (created)
  tasker/.gitignore (created)
  tasker/.metadata (created)
  tasker/ios/Runner/AppDelegate.h (created)
  tasker/ios/Runner/main.m (created)
  tasker/ios/Runner/AppDelegate.m (created)
  tasker/ios/Runner.xcodeproj/project.pbxproj (created)
  tasker/android/app/src/main/res/mipmap-mdpi/ic_launcher.png (created)
  tasker/android/app/src/main/res/mipmap-hdpi/ic_launcher.png (created)
  tasker/android/app/src/main/res/drawable/launch_background.xml (created)
  tasker/android/app/src/main/res/mipmap-xxxhdpi/ic_launcher.png (created)
  tasker/android/app/src/main/res/mipmap-xxhdpi/ic_launcher.png (created)
  tasker/android/app/src/main/res/values/styles.xml (created)
  tasker/android/app/src/main/res/mipmap-xhdpi/ic_launcher.png (created)
  tasker/android/app/src/main/AndroidManifest.xml (created)
  tasker/android/gradle/wrapper/gradle-wrapper.properties (created)
  tasker/android/gradle.properties (created)
  tasker/android/settings.gradle (created)
  tasker/pubspec.yaml (created)
  tasker/README.md (created)
  tasker/lib/main.dart (created)
  tasker/android/app/build.gradle (created)
  tasker/android/app/src/main/java/com/example/tasker/MainActivity.java (created)
  tasker/android/build.gradle (created)
  tasker/android/tasker_android.iml (created)
  tasker/.idea/runConfigurations/main_dart.xml (created)
  tasker/.idea/libraries/Flutter_for_Android.xml (created)
  tasker/.idea/libraries/Dart_SDK.xml (created)
  tasker/.idea/libraries/KotlinJavaRuntime.xml (created)
  tasker/.idea/modules.xml (created)
  tasker/.idea/workspace.xml (created)
Running "flutter packages get" in tasker...                  2.1s
Wrote 64 files.

All done!
[✓] Flutter is fully installed. (Channel beta, v1.0.0, on Mac OS X 10.13.6 17G3025, locale en-US)
[✓] Android toolchain - develop for Android devices is fully installed. (Android SDK 27.0.3)
[!] iOS toolchain - develop for iOS devices is partially installed; more components are available.
    (Xcode 10.1)
[✓] Android Studio is fully installed. (version 3.1)
[✓] VS Code is fully installed. (version 1.29.1)
[✓] Connected device is fully installed. (1 available)

Run "flutter doctor" for information about installing additional components.

In order to run your application, type:

  $ cd tasker
  $ flutter run

Your application code is in tasker/lib/main.dart.
```

### Edit the Generated Code to Create a Blank App
As the output stated, the application code is in the lib directory in the main.dart file. Flutter creates a demo app with tons of comments. If you are like me, you may find this initial outout overwhelming and confusing. 

The first thing I do is edit the application code to dramatically simplify it so it is easier to understand and modify. I also rename the class names while I am at it:

```
import 'package:flutter/material.dart';

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
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Tasker"),
      ),
      body: Container(),
    );
  }
}
```

You can run the code from your IDE, or use the flutter CLI. Assuming you are inside the tasker directory, that would like this:

```
$ flutter run
```

I prefer to use Visual Studio Code's "Run Without Debugging" command.

After running this code, you get a blank application, because the body of the code is simply a blank container.

![blank app](../assets/blank-app.png)

## Import rapido
### Get the Package
Next step is to import rapido into your project. It is probably wise to visit rapido at [pub.dartlang.org](https://pub.dartlang.org/packages/rapido) to check for the latest version. 

To get a flutter package into your project, you add it to your pubspec.yaml file as a dependency. Be careful with your YAML, it cares a lot about proper indentation. Add a reference to rapido so that your pubspec.yaml looks like this:

```
dependencies:
  flutter:
    sdk: flutter
  rapido: ^0.0.11
```

Again, the indentation levels are very important. If the rapido package on pub.dartlang.org is at a different version than is documented here, use the version on pub.dartlang.org.

It is likely that your IDE has run the "packages get" command for you, but if not, again, assuming you are in the tasker directory, run the command:

```
$ flutter packages get
```

At this point the Rapido package should be available to your code.

### Add the Import Statement
To actually use Rapido in your code, you need to import it into you main.dart file.

Add this import to the top of that file right under the existing import:

```
import 'package:rapido/documents.dart';
```

This means that we are going to use the documents capabilities from the rapido package, which is all that is available so far.

If your IDE says that it can't find the package, than most likely you have not run packages get, or you have problems with indenting in your YAML.

## Define a DocumentList
Now it is finally time to write some code by creating a DocumentList. 

## Create the UI




