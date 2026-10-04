---
id: software.testes.tranche15.000947
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://nexte.st/docs/", "https://nexte.st/docs/running/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# nextest: reutilizar binários com archive

## Em uma frase
O comando de arquivamento empacota os binários de teste compilados para que outra etapa ou máquina execute o mesmo build sem recompilar.

## Por que importa
Em pipelines com muitos executores, compilar em cada shard desperdiça tempo e pode introduzir diferenças entre os ambientes de execução.

## Como funciona
Gere o arquivo uma vez, transporte-o para as etapas de execução e rode o nextest apontando para o arquivo recebido.

## Exemplo
`cargo nextest archive --archive-file testes.tar.zst` cria o pacote, e a execução usa `cargo nextest run --archive-file testes.tar.zst`.

## Limites e trade-offs
O arquivo precisa ser gerado para a mesma plataforma de destino e revisão; binários incompatíveis falham na execução ou, pior, produzem resultado enganoso.

## Como verificar
Compare a lista de testes e os resultados entre a execução direta e a execução a partir do arquivo para confirmar a equivalência.

## Conexões
- [[nextest-junit-report]] — Veja também: nextest: publicar resultado em JUnit XML.
- [[nextest-doctests-boundary]] — Veja também: nextest: reconhecer o limite dos doctests.

## Fontes
- [nextest — Documentation](https://nexte.st/docs/) — visão geral do runner, instalação e operação; consultado em 2026-10-02.
- [nextest — Running tests](https://nexte.st/docs/running/) — execução, filtros, saída, listagem e testes ignorados; consultado em 2026-10-02.
