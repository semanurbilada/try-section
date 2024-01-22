// Beginner Console project for practicing C# 
// IDE: Visual Studio 
// Console Game - Number Guesser
using System;

namespace NumberGuesser
{
    // Main Class
    class Program
    {
        // Entry Point Method
        static void Main(string[] args)
        {
            GetAppInfo();

            GreetUser();

            while(true) {

                // Init correct number & guess variable:
                int guess = 0;
                Random random = new Random();
                int correctNum = random.Next(1, 10);

                Console.WriteLine("\nCan you guess a number between 1 - 10?\n");

                // While guess is not correct
                while (guess != correctNum)
                {
                    string input = Console.ReadLine();

                    // Check input is a number
                    if (!int.TryParse(input, out guess))
                    {
                        PrintColorMessage(
                            ConsoleColor.Red,
                            message: "\nWrong type, please enter a number!\n"
                        );
                        continue;
                    }

                    // Cast to int and put in guess
                    guess = Int32.Parse(input);

                    // Match guess to correct number
                    if (guess != correctNum)
                    {
                        PrintColorMessage(
                           ConsoleColor.Red,
                           message: "\nWrong number, please try again!\n"
                        );
                    }
                }

                PrintColorMessage(
                    ConsoleColor.Yellow,
                    message: "\nYou find out. Congrats!!!"
                );

                Console.WriteLine("\nHey, you wanna play again? [Y or N]\n");
                string answer = Console.ReadLine().ToUpper();

                if( answer == "Y" ) {
                    continue;
                }
                else if( answer == "N" ) {
                    return;
                }
                else {
                    return;
                }
            }
        }

        static void GetAppInfo() {
            string appName = "Number Guesser";
            string appVersion = "1.0.0";
            string appAuthor = "Semanur Bilada";

            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("Welcome to {0}!\nVersion {1} by {2}", appName, appVersion, appAuthor);

            Console.ForegroundColor = ConsoleColor.Cyan;
        }

        static void GreetUser() {
            Console.WriteLine("\nType your name : ");

            Console.WriteLine("\nHello {0}, let's start the game!", Console.ReadLine());

            // Note: if else can be added here for input type of name
        }

        static void PrintColorMessage( ConsoleColor color, string message ) {
            Console.ForegroundColor = color;
            Console.WriteLine(message);
            Console.ResetColor();
        }
    }
} 