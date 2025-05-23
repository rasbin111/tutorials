package main

import (
	"context"
	"fmt"
	"log"
	"os"

	"github.com/jackc/pgx/v5/pgxpool"
	"github.com/joho/godotenv"
)

var pool *pgxpool.Pool

func init() {
	err := godotenv.Load()
	if err != nil {

		log.Fatal("Error loading .env file")
	}

	connectionStr := fmt.Sprintf("postgres://%s:%s@%s:%s/%s",
		os.Getenv("DB_USER"),
		os.Getenv("DB_PASSWORD"),
		os.Getenv("DB_HOST"),
		os.Getenv("DB_PORT"),
		os.Getenv("DB_NAME"),
	)

	pool, err = pgxpool.New(context.Background(), connectionStr)

	if err != nil {
		log.Fatalf("Unable to connect to database: %v\n", err)
	}

	fmt.Println("Connected to PostgreSQL Database")

}

func main() {
	defer pool.Close()

	creationErr := CreateUser("Ravi Karki", "ravi@gmail.com", "Ramechhap")

	if creationErr != nil {
		log.Fatalf("Unable to create user: %v\n", creationErr)
	}

}
