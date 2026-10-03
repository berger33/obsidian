---
id: software.testes.tranche18.001228
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-18.md"
fontes: ["https://semgrep.dev/docs/", "https://github.com/semgrep/semgrep"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Semgrep: estruturar uma regra própria

## Em uma frase
Uma regra declara identificador, linguagem, severidade, mensagem e o padrão que deve corresponder ao código analisado.

## Por que importa
Padrões escritos na forma do código facilitam revisar a intenção da regra e ajustá-la sem conhecimento profundo de análise estática.

## Como funciona
Nomeie a regra de forma descritiva, declare a linguagem correta e escreva mensagem que explique o problema e a ação esperada.

## Exemplo
Uma regra para detectar comparação de senha com igualdade simples pode ser escrita na forma da própria expressão.

## Limites e trade-offs
Linguagem declarada incorretamente faz a regra não encontrar nada, e mensagens genéricas dificultam entender o achado.

## Como verificar
Aplique a regra a um trecho que sabidamente contém o problema e confirme que o achado aponta a linha correta.

## Conexões
- [[semgrep-pattern-operators]] — Veja também: Semgrep: combinar condições com operadores.

## Fontes
- [Semgrep — Documentation](https://semgrep.dev/docs/) — instalação, execução, integração contínua, supressões e severidade; consultado em 2026-10-03.
- [Semgrep — repositório oficial](https://github.com/semgrep/semgrep) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
