package main

import (
	"context"
	"fmt"
)

func GetUserById(id int) error {
	user := User{}
	err := pool.QueryRow(context.Background(), "select * from \"User\" where id=1").Scan(&user.ID, &user.Name, &user.Email, &user.Address)
	if err != nil {
		return err
	}
	fmt.Printf("User: %v\n", user)
	return nil
}

func CreateUser(name string, email string, address string) error {
	user := User{}
	insertString := `INSERT INTO "User" (name, email, address)
			VALUES ($1, $2, $3)
			RETURNING id, name, email, address`
	err := pool.QueryRow(context.Background(), insertString, name, email, address).Scan(&user.ID, &user.Name, &user.Email, &user.Address)

	if err != nil {
		return err
	}

	fmt.Printf("Created user: %v\n", user)
	return nil
}
