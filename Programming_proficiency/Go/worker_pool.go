package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

// Task represents a unit of work
type Task struct {
	ID      int
	Payload int
}

// Result represents the result of a task
type Result struct {
	TaskID int
	Output int
}

// Worker processes tasks from the task channel and sends results to the result channel
func Worker(id int, tasks <-chan Task, results chan<- Result, wg *sync.WaitGroup) {
	defer wg.Done()
	for task := range tasks {
		fmt.Printf("Worker %d processing task %d\n", id, task.ID)
		time.Sleep(time.Duration(rand.Intn(1000)) * time.Millisecond) // Simulate work
		output := task.Payload * 2 // Example task processing
		results <- Result{TaskID: task.ID, Output: output}
	}
}

func main() {
	rand.Seed(time.Now().UnixNano())

	// Create channels
	tasks := make(chan Task, 10)
	results := make(chan Result, 10)

	// WaitGroup to wait for all workers to finish
	var wg sync.WaitGroup

	// Start workers
	numWorkers := 3
	for i := 1; i <= numWorkers; i++ {
		wg.Add(1)
		go Worker(i, tasks, results, &wg)
	}

	// Generate tasks
	numTasks := 5
	for i := 1; i <= numTasks; i++ {
		tasks <- Task{ID: i, Payload: rand.Intn(100)}
	}
	close(tasks)

	// Wait for all workers to finish
	go func() {
		wg.Wait()
		close(results)
	}()

	// Collect results
	for result := range results {
		fmt.Printf("Task %d processed with result %d\n", result.TaskID, result.Output)
	}

	fmt.Println("All tasks processed.")
}
