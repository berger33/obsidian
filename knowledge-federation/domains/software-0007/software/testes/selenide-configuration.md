---
id: software.testes.tranche20.001405
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
fontes: ["https://selenide.org/faq.html", "https://github.com/selenide/selenide"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Selenide: configurar navegador e limites

## Em uma frase
As propriedades definem navegador, endereço remoto, tamanho de janela, limite de espera, captura de tela e pasta de downloads.

## Por que importa
A configuração centralizada evita repetir ajustes em cada teste e mantém comportamento igual entre máquinas e esteira.

## Como funciona
Mantenha o padrão em arquivo de propriedades, sobrescreva por execução quando necessário e configure o navegador remoto antes de abrir a página.

## Exemplo
O ambiente de integração pode rodar sem interface gráfica, com tamanho de janela fixo e captura de tela habilitada.

## Limites e trade-offs
Configurar o endereço remoto depois de abrir o navegador não tem efeito, e janelas de tamanhos diferentes entre máquinas geram falhas de layout.

## Como verificar
Compare uma execução local e outra no ambiente automatizado e confirme que as propriedades produzem o mesmo comportamento.

## Conexões
- [[selenide-screenshots-and-reports]] — Veja também: Selenide: registrar evidências e relatórios.
- [[selenide-headless-and-parallel]] — Veja também: Selenide: executar sem interface e em paralelo.

## Fontes
- [Selenide — Perguntas frequentes](https://selenide.org/faq.html) — configuração, navegadores, grade e boas práticas; consultado em 2026-10-03.
- [Selenide — repositório oficial](https://github.com/selenide/selenide) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
