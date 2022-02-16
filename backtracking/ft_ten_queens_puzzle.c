/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_ten_queens_puzzle.c                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jsuh <jsuh@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/02/16 09:23:18 by jsuh              #+#    #+#             */
/*   Updated: 2022/02/16 10:01:25 by jsuh             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdio.h>

int arr[10][10] = {0,};
int p_arr[10] = {0,};
int g_cnt = 0;

void    ft_putchar(char c)
{
    write(1, &c, 1);
}

void    ft_printInt(int c)
{   
    if (c == 0)
        return;
    int r;
    r = c % 10;
    c = c / 10;
    ft_printInt(c);
    ft_putchar(r + '0');
}

int rowCheck(int row, int col) {
    int i = 0;
    while (i < 10)
        if (arr[row][i++] != 0)
            return (0);
    i = 0;
    while (i < 10)
        if (arr[i++][col] != 0)
            return (0);
    return (1);
}

int diagCheck(int row, int col) {
    int r = row;
    int c = col;
    while (row != -1 && col != -1)
        if (arr[row--][col--] != 0)
            return (0);
    while(r != -1 && c != 10)
        if (arr[r--][c++] != 0)
            return (0);
    return (1);
}

void    print_arr(int *a)
{
    int i = 0;
    while (i < 10)
        ft_putchar(a[i++] + '0');
    write(1, "\n", 1);
}
void    ten_queen(int row, int col)
{
    if (row == 10)
    {
        print_arr(p_arr);
        g_cnt++;
        return;
    }
    else
    {
	while (col < 10)
	{
		if (rowCheck(row, col) && diagCheck(row, col))
		{
			arr[row][col] = 1;
                	p_arr[row] = col;
                	ten_queen(row + 1, 0);
                	arr[row][col] = 0;
                	p_arr[row] = 0;
		}
			col++;
		}
    }
}

void    ft_ten_queens_puzzle(void)
{
    ten_queen(0, 0);
    ft_printInt(g_cnt);
    write(1, "\n", 1);
}

int main(void)
{
    ft_ten_queens_puzzle();
    return (0);
}
