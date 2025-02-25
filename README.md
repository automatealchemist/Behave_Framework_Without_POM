# **Behave Framework Without POM**  
A BDD-Based Behave Framework with Allure Reports  

## **Overview**  
This repository contains a **Behavior-Driven Development (BDD) framework** using **Behave** without the Page Object Model (POM). It includes:  
- **Feature files** (BDD Scenarios)  
- **Step definitions** (Implementation of steps)  
- **Environment file** (Setup and teardown methods)  
- **Allure report integration** for test reporting  

## **Execution and Report Generation**  

### **Running the Feature Files**  
To execute all feature files and generate Allure reports in JSON format, use the following command:  

```sh
behave -f allure_behave.formatter:AllureFormatter -o reports features
```

- This will run all feature files present in the `features` directory.  
- The results will be stored in the `reports/` folder in JSON format.  

### **Generating the Allure Report (HTML Format)**  
To generate and view the Allure report in an HTML format, run:  

```sh
allure serve reports/
```

- This command processes the JSON reports and generates an interactive Allure report in a temporary directory.  
- The report provides insights into test execution, including passed, failed, and skipped tests.  

## **Prerequisites**  

To set up and run this framework, ensure the following dependencies are installed:  

1. **Python IDE** – [PyCharm](https://www.jetbrains.com/pycharm/) or [VS Code](https://code.visualstudio.com/)  
2. **Gherkin Plugin** – Required for syntax highlighting and BDD support  
3. **Behave** – Install using:  

   ```sh
   pip install behave
   ```  

4. **Allure Reports** – Install using:  

   ```sh
   pip install allure-behave
   ```  

   **Note:** You must also install **Allure Command Line** separately. Follow the [official Allure installation guide](https://docs.qameta.io/allure/#_installing) based on your OS.  

## **How to Use This Repository**  

1. **Fork the repository** to your GitHub account.  
2. **Clone the repository** to your local machine:  

   ```sh
   git clone https://github.com/your-username/Behave_Framework_Without_POM.git
   ```  

3. **Navigate to the project directory:**  

   ```sh
   cd Behave_Framework_Without_POM
   ```  

4. **Install dependencies:**  

   ```sh
   pip install -r requirements.txt
   ```  

5. **Run the tests and generate reports as described above.**  

## **Contributing**  
If you find this framework useful, feel free to contribute by submitting pull requests or sharing it with others.  
