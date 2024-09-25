/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test_evaluator.js                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jduong22 <juha.duong@edu.turkuamk.fi>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/09/25 19:24:34 by jduong22          #+#    #+#             */
/*   Updated: 2024/09/25 19:28:19 by jduong22         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

const evaluator = require('./evaluator');

// Define the evaluation scale
const scale = [
    { grade: 1, points: 20 },
    { grade: 2, points: 35 },
    { grade: 3, points: 50 },
    { grade: 4, points: 65 },
    { grade: 5, points: 80 }
];

// Set the evaluation scale
evaluator.setEvaluationScale(scale);

// Test cases
console.log(evaluator.getGrade(10)); // Expected output: 0
console.log(evaluator.getGrade(20)); // Expected output: 1
console.log(evaluator.getGrade(35)); // Expected output: 2
console.log(evaluator.getGrade(50)); // Expected output: 3
console.log(evaluator.getGrade(65)); // Expected output: 4
console.log(evaluator.getGrade(80)); // Expected output: 5
console.log(evaluator.getGrade(90)); // Expected output: 5

// Test case when evaluation scale is not set
const evaluatorWithoutScale = require('./evaluator');
console.log(evaluatorWithoutScale.getGrade(50)); // Expected output: 'There is no evaluation scale defined.'