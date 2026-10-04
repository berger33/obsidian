---
id: software.testes.tranche18.001247
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
fontes: ["https://trivy.dev/latest/docs/", "https://github.com/aquasecurity/trivy"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Trivy: reconhecer limites da varredura

## Em uma frase
A ferramenta encontra componentes conhecidos e padrões de configuração, mas não substitui análise de falhas de lógica nem testes de invasão.

## Por que importa
Uma varredura limpa não significa artefato seguro, e confiar apenas nela deixa caminhos de exploração sem avaliação.

## Como funciona
Combine a varredura com testes de comportamento, revisão de dependências e análise de fluxo, mantendo as bases atualizadas e os artefatos identificados por versão.

## Exemplo
Um artefato sem vulnerabilidades conhecidas ainda pode falhar por configuração de autenticação incorreta na aplicação.

## Limites e trade-offs
Bases de vulnerabilidades têm atraso e cobertura variável entre ecossistemas, e achados sem correção exigem mitigação alternativa.

## Como verificar
Escolha uma varredura considerada limpa e liste quais riscos ela explicitamente não cobre antes de usá-la como evidência.

## Conexões
- [[trivy-formats-and-output]] — Veja também: Trivy: escolher formato de saída.

## Fontes
- [Trivy — Documentation](https://trivy.dev/latest/docs/) — alvos, verificadores, políticas, exceções e formatos de saída; consultado em 2026-10-03.
- [Trivy — repositório oficial](https://github.com/aquasecurity/trivy) — código-fonte, alvos suportados e documentação do projeto; consultado em 2026-10-03.
