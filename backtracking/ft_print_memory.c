/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jsuh <jsuh@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/02/16 09:23:43 by jsuh              #+#    #+#             */
/*   Updated: 2022/02/16 09:39:32 by jsuh             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void    ft_putchar(char c)
{
    write(1, &c, 1);
}

void ft_printInt(int c)
{   
    if (c == 0)
        return;
    int r;
    r = c % 10;
    c = c / 10;
    ft_printInt(c);
    ft_putchar(r + '0');
}

int main(void)
{
    ft_printInt(123);
    return (0);
}