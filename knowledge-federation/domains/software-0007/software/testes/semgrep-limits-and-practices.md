---
id: software.testes.tranche18.001237
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
fontes: ["https://semgrep.dev/docs/", "https://semgrep.dev/docs/writing-rules/overview"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Semgrep: reconhecer limites da análise estática

## Em uma frase
A análise identifica padrões e fluxos modelados, mas não substitui execução, revisão de projeto nem testes de comportamento.

## Por que importa
Tratar a análise como verificação completa dá falsa segurança sobre classes de problema que exigem execução do sistema.

## Como funciona
Combine análise estática com testes automatizados, revisão de código e verificação de dependências, tratando cada uma pelo que cobre.

## Exemplo
Uma regra pode mostrar que a validação existe no código sem provar que ela funciona para todas as entradas.

## Limites e trade-offs
Achados de análise não indicam exploração possível, e a ausência de achados não indica ausência de vulnerabilidade.

## Como verificar
Escolha um achado e escreva o teste que demonstra se o caminho é realmente explorável antes de decidir a prioridade.

## Conexões
- [[semgrep-custom-rules]] — Veja também: Semgrep: manter regras próprias do projeto.

## Fontes
- [Semgrep — Documentation](https://semgrep.dev/docs/) — instalação, execução, integração contínua, supressões e severidade; consultado em 2026-10-03.
- [Semgrep — Writing rules](https://semgrep.dev/docs/writing-rules/overview) — estrutura de regra, operadores, metavariáveis e modo de propagação; consultado em 2026-10-03.
