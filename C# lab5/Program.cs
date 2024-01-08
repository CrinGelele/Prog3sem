//файл Program.cs
using System;
using static System.Math;
using levenstain;

Levenstain_pair pair = new Levenstain_pair(Console.ReadLine(), Console.ReadLine());
pair.Print_matrix();
Console.WriteLine(pair.Get_distance());