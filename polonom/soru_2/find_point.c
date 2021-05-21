// find_point.c
#include <stdio.h>
#include <stdlib.h>

int inside_rectangle(int xy[], int p[])
{
    if (((p[0] - xy[0]) * (xy[2] - p[0]) >= 0) && (((p[1] - xy[1]) * (xy[2] - p[1]) >= 0)))
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int main()
{
    int point[2];
    int canvas[2];
    int N = 0;
    int counter = 0;

    printf("Enter canvas size: ");
    scanf("%d %d", &canvas[0], &canvas[1]);
    printf("Enter pointer coordinates: ");
    scanf("%d %d", &point[0], &point[1]);
    printf("Enter number of rectangles: ");

    scanf("%d", &N);
    int(*rectangles)[4] = malloc(sizeof(int[N][4]));
    for (int i = 0; i < N; i++)
    {
        printf("Enter %d. rectangle coordinates: ", i + 1);
        scanf("%d %d %d %d", &rectangles[i][0], &rectangles[i][1], &rectangles[i][2], &rectangles[i][3]);
        if (inside_rectangle(rectangles[i], point))
        {
            counter++;
        }
    }

    printf("point inside of %d rectangles\n", counter);

    return 0;
}