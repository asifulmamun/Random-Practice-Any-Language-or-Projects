#include <graphics.h>
#include <stdio.h>

void bresenham_circle(int x0, int y0, int radius)
{
    int x = 0, y = radius;
    int p = 3 - 2 * radius;

    while (x <= y)
    {
        // plot eight-way symmetric points
        putpixel(x0 + x, y0 + y, WHITE);
        putpixel(x0 - x, y0 + y, WHITE);
        putpixel(x0 + x, y0 - y, WHITE);
        putpixel(x0 - x, y0 - y, WHITE);
        putpixel(x0 + y, y0 + x, WHITE);
        putpixel(x0 - y, y0 + x, WHITE);
        putpixel(x0 + y, y0 - x, WHITE);
        putpixel(x0 - y, y0 - x, WHITE);

        // update the decision parameter
        if (p < 0)
        {
            p += 4 * x + 6;
        }
        else
        {
            p += 4 * (x - y) + 10;
            y--;
        }
        x++;
    }
}
#include <graphics.h>
#include <stdio.h>

void bresenham_circle(int x0, int y0, int radius)
{
    int x = 0, y = radius;
    int p = 3 - 2 * radius;

    while (x <= y)
    {
        // plot eight-way symmetric points
        putpixel(x0 + x, y0 + y, WHITE);
        putpixel(x0 - x, y0 + y, WHITE);
        putpixel(x0 + x, y0 - y, WHITE);
        putpixel(x0 - x, y0 - y, WHITE);
        putpixel(x0 + y, y0 + x, WHITE);
        putpixel(x0 - y, y0 + x, WHITE);
        putpixel(x0 + y, y0 - x, WHITE);
        putpixel(x0 - y, y0 - x, WHITE);

        // update the decision parameter
        if (p < 0)
        {
            p += 4 * x + 6;
        }
        else
        {
            p += 4 * (x - y) + 10;
            y--;
        }
        x++;
    }
}

int main()
{
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    int x0 = 250, y0 = 250, radius = 100;
    bresenham_circle(x0, y0, radius);

    getch();
    closegraph();
    return 0;
}