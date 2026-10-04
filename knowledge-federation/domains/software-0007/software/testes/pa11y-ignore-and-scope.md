---
id: software.testes.tranche16.001029
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-16.md"
fontes: ["https://github.com/pa11y/pa11y", "https://github.com/pa11y/pa11y-ci"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pa11y: restringir escopo e registrar exceções

## Em uma frase
Regras específicas podem ser ignoradas, e a análise pode ser limitada a um elemento raiz ou excluir trechos selecionados da página.

## Por que importa
Nem todo achado é acionável, e exceções precisam ser estreitas e justificadas para não esconder problemas reais.

## Como funciona
Ignore códigos pontuais com comentário de contexto, limite a varredura a regiões sob responsabilidade do time e oculte apenas conteúdo de terceiros.

## Exemplo
Componentes de terceiros embutidos podem ser ocultados da varredura enquanto o restante da página permanece sendo analisado.

## Limites e trade-offs
Ignorar por tipo inteiro remove categorias relevantes, e esconder trechos grandes reduz a cobertura justamente onde os problemas costumam aparecer.

## Como verificar
Remova temporariamente uma exceção e verifique quantos problemas ela estava suprimindo, avaliando se a justificativa continua válida.

## Conexões
- [[pa11y-threshold-policy]] — Veja também: Pa11y: usar limite como política temporária.
- [[pa11y-config-file]] — Veja também: Pa11y: centralizar configuração do projeto.

## Fontes
- [Pa11y — repositório oficial](https://github.com/pa11y/pa11y) — linha de comando, padrões, motores, ações, relatórios e limites; consultado em 2026-10-03.
- [Pa11y CI — repositório oficial](https://github.com/pa11y/pa11y-ci) — varredura de múltiplas páginas, configuração e integração contínua; consultado em 2026-10-03.
