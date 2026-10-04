---
id: software.testes.tranche20.001446
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-20.md"
fontes: ["https://github.com/robolectric/robolectric", "https://robolectric.org/getting-started/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Robolectric: integrar com bibliotecas de teste

## Em uma frase
A execução convive com bibliotecas de asserção, dublês e execução paralela, mantendo o mesmo padrão dos testes comuns.

## Por que importa
Manter o padrão da suíte evita dois estilos de teste e permite reutilizar infraestrutura e relatórios já existentes no projeto.

## Como funciona
Use as bibliotecas de asserção habituais, isole o estado entre casos e evite depender de ordem entre testes da mesma classe.

## Exemplo
Um caso pode combinar verificação de comportamento com dublês de rede, mantendo o mesmo formato dos testes de lógica pura.

## Limites e trade-offs
Misturar estilos e compartilhar estado entre casos gera falhas dependentes de ordem, e paralelismo sem isolamento produz intermitência.

## Como verificar
Execute a classe em ordem invertida e com paralelismo e confirme que os resultados não mudam.

## Conexões
- [[robolectric-dependencies-and-offline]] — Veja também: Robolectric: gerenciar dependências de execução.
- [[robolectric-vs-instrumented]] — Veja também: Robolectric: escolher entre JVM e execução instrumentada.

## Fontes
- [Robolectric — repositório oficial](https://github.com/robolectric/robolectric) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
- [Robolectric — Primeiros passos](https://robolectric.org/getting-started/) — configuração do projeto, executor e ciclo de vida de telas; consultado em 2026-10-03.
