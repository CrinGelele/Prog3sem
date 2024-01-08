//Файл levenstain.cs библиотеки
namespace levenstain
{
    using static System.Math;
    public class Levenstain_pair
    {
        public string String1 { get; set; } = "";
        public string String2 { get; set; } = "";

        public Levenstain_pair(string string1, string string2) { String1  = string1; String2 = string2; }

        private static int Minimum(int a, int b, int c) { return Min(Min(a, b), c);  }
        private int[,] Get_matrix ()
        {
            int n = String1.Length + 1;
            int m = String2.Length + 1;
            var matrix = new int[n, m];
            for (int i = 0; i < n; i++) { matrix[i, 0] = i; }
            for (int j = 0; j < m; j++) { matrix[0, j] = j; }
            for (int i = 1; i < n; i++)
            {
                for (int j = 1; j < m; j++)
                {
                    int sub_cost = String1[i - 1] == String2[j - 1] ? 0 : 1;
                    matrix[i, j] = Minimum(matrix[i - 1, j] + 1,
                                       matrix[i, j - 1] + 1,
                                       matrix[i - 1, j - 1] + sub_cost);
                }
            }
            return matrix;
        }

        public void Print_matrix ()
        {
            for (int i = 0; i < String1.Length; i++)
            {
                for (int j = 0; j < String2.Length; j++)
                {
                    Console.Write(Get_matrix()[i, j] + "\t");
                }
                Console.WriteLine();
            }
        }
        public int Get_distance () { return Get_matrix()[String1.Length, String2.Length]; }

    }
}
