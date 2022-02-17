/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_memory.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jsuh <jsuh@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/02/16 16:54:58 by jsuh              #+#    #+#             */
/*   Updated: 2022/02/17 18:12:59 by jsuh             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void    ft_putchar(char c)
{
    write(1, &c, 1);
}

void    r_to_a(unsigned long r)
{
    switch(r) {
    case 10:
        ft_putchar('a');
        break;
    case 11:
        ft_putchar('b');
        break;
    case 12:
        ft_putchar('c');
        break;
    case 13:
        ft_putchar('d');
        break;
    case 14:
        ft_putchar('e');
        break;
    case 15:
        ft_putchar('f');
        break;
    }
}

void    print_memory(unsigned long c, int cnt)
{   
    if (c == 0)
    {
        int i = 0;
        while (i++ < 16 - cnt)
            ft_putchar('0');
    }   
    if (c > 0)
    {
        unsigned long r = c % 16;
        c = c / 16;
        print_memory(c, cnt + 1);
        if (r <= 9)
          ft_putchar(r + '0');
        else
            r_to_a(r);
    }
}

void    a_to_hex(unsigned long c)
{   
    if (c == 0)
        return; 
    if (c > 0)
    {
        unsigned long r = c % 16;
        c = c / 16;
        a_to_hex(c);
        if (r <= 9)
          ft_putchar(r + '0');
        else
            r_to_a(r);
    }
}

int is_printable(char c)
{
    if ((9 <= c && c <= 13) || (32 <= c && c<= 126))
        return (1);
    return (0);
}

void    print_total(char *str, unsigned int i, int cnt, int size)
{
    int q = size / 16;
    int r = size % 16;
    while (++i < size && str[i])
    {
        if (i % 16 == 0)
        {
            print_memory((unsigned long)&str[i], 0);
            write(1, ": ", 2);
        }
        if (is_printable(str[i]) && (cnt % 2 == 0))
        {
            a_to_hex((unsigned long)str[i]);
            ft_putchar(' ');
        }
        else if (is_printable(str[i]) && (cnt % 2 == 1))
            a_to_hex((unsigned long)str[i]);
        else if (!(is_printable(str[i])))
            ft_putchar('.');
        else if (!(is_printable(str[i])) && cnt % 2 == 0)
            write(1, ". ", 1);
        cnt++;
    }
}

void    *ft_print_memory(void *addr, unsigned int size)
{
    char *str = (char *)(addr);
    print_total(str, -1, 1, size);
    return (void *)(str);
}

int main(void)
{
    char str[] = "Bonjour les aminc";
    ft_print_memory(str, 18);
    return (0);
}