

package MyBasicPrograms;

import javafx.application.Application;
import javafx.scene.control.Button;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;

public class JavaFX extends Application {
	public static void main(String[] args) {
		launch(args);
	}

	@Override
	public void start(Stage primaryStage) throws Exception {
		Button btn = new Button("Click me");

		StackPane root = new StackPane();

		primaryStage.show();

	}

}
