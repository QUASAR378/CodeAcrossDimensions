#include <iostream>
#include <cmath>

using namespace std;

double celsiusToFahrenheit(double celsius) {
    return (celsius * 9.0 / 5.0) + 32.0;
}
double fahrenheitToCelsius(double fahrenheit) {
    return (fahrenheit - 32.0) * 5.0 / 9.0;
}
double celsiusToKelvin(double celsius) {
    return celsius + 273.15;
}
double kelvinToCelsius(double kelvin) {
    return kelvin - 273.15;
}
double fahrenheitToKelvin(double fahrenheit) {
    return celsiusToKelvin(fahrenheitToCelsius(fahrenheit));
}
double kelvinToFahrenheit(double kelvin) {
    return celsiusToFahrenheit(kelvinToCelsius(kelvin));
}
void displayMenu() {
    cout << "Temperature Conversion Menu:" << endl;
    cout << "1. Celsius to Fahrenheit" << endl;
    cout << "2. Fahrenheit to Celsius" << endl;
    cout << "3. Celsius to Kelvin" << endl;
    cout << "4. Kelvin to Celsius" << endl;
    cout << "5. Fahrenheit to Kelvin" << endl;
    cout << "6. Kelvin to Fahrenheit" << endl;
    cout << "7. Exit" << endl;
    cout << "Choose an option (1-7): ";
}
int main() {
    int choice;
    double temperature, convertedTemp;

    do {
        displayMenu();
        cin >> choice;

        if (choice >= 1 && choice <= 6) {
            cout << "Enter temperature: ";
            cin >> temperature;
        }

        switch (choice) {
            case 1:
                convertedTemp = celsiusToFahrenheit(temperature);
                cout << temperature << " °C = " << convertedTemp << " °F" << endl;
                break;
            case 2:
                convertedTemp = fahrenheitToCelsius(temperature);
                cout << temperature << " °F = " << convertedTemp << " °C" << endl;
                break;
            case 3:
                convertedTemp = celsiusToKelvin(temperature);
                cout << temperature << " °C = " << convertedTemp << " K" << endl;
                break;
            case 4:
                convertedTemp = kelvinToCelsius(temperature);
                cout << temperature << " K = " << convertedTemp << " °C" << endl;
                break;
            case 5:
                convertedTemp = fahrenheitToKelvin(temperature);
                cout << temperature << " °F = " << convertedTemp << " K" << endl;
                break;
            case 6:
                convertedTemp = kelvinToFahrenheit(temperature);
                cout << temperature << " K = " << convertedTemp << " °F" << endl;
                break;
            case 7:
                cout << "Exiting the program." << endl;
                break;
            default:
                cout << "Invalid choice. Please try again." << endl;
        }
        cout << endl;
    } while (choice != 7);

    return 0;
}