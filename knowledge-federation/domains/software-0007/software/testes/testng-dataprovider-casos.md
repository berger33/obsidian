---
id: software.testes.tranche12.000570
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-12.md"
fontes: ["https://testng.org/annotations.html", "https://testng.org/parameters.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# TestNG: alinhar DataProvider e assinatura do teste

## Em uma frase
`@DataProvider` associa conjuntos de argumentos a uma função `@Test`, e cada linha retornada precisa ser atribuível aos parâmetros daquele método.

## Por que importa
Uma tabela bem formada amplia combinações de entrada sem copiar o corpo do teste e mantém os valores que falham visíveis como casos distintos.

## Como funciona
Declare o provider próximo do teste ou em uma classe dedicada, atribua-lhe um nome estável e confira a quantidade, ordem e tipos das colunas contra a assinatura consumidora.

## Exemplo
Um provider pode devolver códigos de país e taxas em pares; o método de teste recebe cada par e valida a conversão para a unidade monetária esperada.

## Limites e trade-offs
Dados em ordem errada ainda podem compilar se os tipos forem compatíveis, mas testar uma combinação diferente da pretendida. Evite esconder a origem do valor em lógica de setup extensa.

## Como verificar
Execute um subconjunto com dados válidos e inválidos, confira a identificação de cada invocação no relatório e confirme que a linha problemática aparece no diagnóstico.

## Conexões
- [[testng-parameters-escopo-xml]] — Veja também: TestNG: organizar parâmetros XML por escopo.

## Fontes
- [TestNG — Annotations](https://testng.org/annotations.html) — ciclo de vida, DataProvider, Factory, Listener e atributos de teste; consultado em 2026-10-02.
- [TestNG — Parameters](https://testng.org/parameters.html) — parâmetros XML, opções, hierarquia de escopo e data providers; consultado em 2026-10-02.
