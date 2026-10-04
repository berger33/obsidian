---
id: software.testes.tranche20.001401
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
fontes: ["https://selenide.org/documentation.html", "https://github.com/selenide/selenide"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Selenide: trabalhar com coleções

## Em uma frase
Consultas com cifrão duplo retornam coleções com filtros, verificação de tamanho e extração de textos e atributos.

## Por que importa
Listas e tabelas são verificadas em conjunto, evitando laços manuais e comparações frágeis elemento a elemento.

## Como funciona
Use verificações de tamanho, filtre por texto ou classe e extraia os valores quando precisar comparar listas completas.

## Exemplo
A verificação pode exigir que a lista de resultados tenha tamanho maior que zero e contenha o item de texto informado.

## Limites e trade-offs
Extrair textos sem esperar o carregamento completo produz lista vazia, e filtros amplos selecionam elementos de blocos vizinhos.

## Como verificar
Acrescente um item à lista em teste e confirme que a verificação de tamanho passa a refletir a nova quantidade.

## Conexões
- [[selenide-smart-waits]] — Veja também: Selenide: confiar nas esperas automáticas.
- [[selenide-page-objects]] — Veja também: Selenide: escrever objetos de página.

## Fontes
- [Selenide — Documentação](https://selenide.org/documentation.html) — API de elementos, coleções, condições e esperas automáticas; consultado em 2026-10-03.
- [Selenide — repositório oficial](https://github.com/selenide/selenide) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
