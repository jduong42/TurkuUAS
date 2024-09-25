/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   evulator.js                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jduong22 <juha.duong@edu.turkuamk.fi>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/09/25 19:26:56 by jduong22          #+#    #+#             */
/*   Updated: 2024/09/25 19:27:35 by jduong22         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

var evaluationScale = null;

function setEvaluationScale(scale) {
    evaluationScale = scale;
}

function getGrade(points) {
    if (!evaluationScale) {
        return 'There is no evaluation scale defined.';
    }

    for (let i = evaluationScale.length - 1; i >= 0; i--) {
        if (points >= evaluationScale[i].points) {
            return evaluationScale[i].grade;
        }
    }

    return 0;
}

module.exports = {
    setEvaluationScale,
    getGrade
};