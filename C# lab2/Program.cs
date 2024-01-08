using System;
using static System.Math;
using Figures;

Rectangle a = new Rectangle(2, 3);
a.Print();
Square b = new Square(3);
b.Print();
Circle c = new Circle(3);
c.Print();

namespace Figures
{
    abstract class Figure
    {
        public abstract double Area();
    }
    internal interface IPrint
    {
        void Print();
    }
    class Rectangle : Figure, IPrint
    {
        public double Width { get; set; } = 0;
        public double Height { get; set; } = 0;
        public Rectangle(double width, double height) { Width = width; Height = height; }
        public override double Area() { return Height * Width; }
        public override string ToString()
        {
            return $"{Width:f2} * {Height:f2} = {Area():f2}";
        }
        public void Print() { Console.WriteLine(ToString()); }
    }

    class Square : Rectangle, IPrint
    {
        public Square(double Width) : base(Width, Width) { } 
        public override double Area() { return Width * Width; }
        public override string ToString()
        {
            return $"{Width:f2} * {Width:f2} = {Area():f2}";
        }
        //public void Print() { Console.WriteLine(ToString() ); } 
    }

    class Circle : Figure, IPrint
    {
        public double Radius { get; set; } = 0;
        public Circle(double radius) { Radius = radius; }
        public override double Area() { return PI * Radius * Radius; }
        public override string ToString()
        {
            return $"pi * {Radius:f2}^2 = {Area():f2}";
        }
        public void Print() { Console.WriteLine(ToString()); }
    }
}

