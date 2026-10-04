---
id: software.criacao_ia.tranche03.000254
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-03.md"
fontes: ["https://openusd.org/release/api/ar_page_front.html", "https://openusd.org/release/api/class_usd_stage.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# OpenUSD: resolver context e asset identifiers de pipeline

## Em uma frase
Um asset path OpenUSD é um identificador entregue a um resolver e não precisa ser um caminho de arquivo local comum.

## Por que importa
Pipelines podem localizar assets em repositórios versionados, armazenamentos remotos ou serviços de produção. Assumir que todos os identifiers são caminhos do sistema de arquivos quebra portabilidade e faz referências relativas dependerem de layout local acidental.

## Como funciona
Asset resolver plugins convertem identifiers em assets efetivos conforme política do site. Um resolver context representa configuração relevante de busca e pode ser associado à abertura do stage; mantenha o contexto consistente ao compor referências, consultar assets e construir caches. Registre identifier lógico separado do caminho resolvido para auditoria e reprodução.

## Exemplo
Uma referência guarda um identifier de asset versionado que o resolver de estúdio mapeia à revisão aprovada no storage central. O mesmo USD abre em workstation e farm porque ambas selecionam o contexto correto, sem reescrever o arquivo com caminho absoluto de uma máquina.

## Limites e trade-offs
Resolver context não garante que asset esteja disponível nem fixa automaticamente uma revisão imutável se a configuração permitir alias mutável. Plugins específicos de site podem aplicar regras próprias e precisam ser instalados em todos os consumidores.

## Como verificar
Abra o mesmo stage com contextos diferentes, registre resolved path e layer identifier e valide que cada referência aponta à revisão esperada. Execute o teste em workstation limpa e worker de farm.

## Conexões
- [[openusd-reference-versus-payload]] — OpenUSD: escolher reference ou payload para composição diferida.
- [[openusd-variants-edit-context]] — OpenUSD: autorar opiniões no variant edit context correto.

## Fontes
- [OpenUSD 26.08 — Asset Resolution](https://openusd.org/release/api/ar_page_front.html) — define asset resolvers, identifiers e contextos de resolução Consulta: 2026-10-04.
- [OpenUSD 26.08 — UsdStage API](https://openusd.org/release/api/class_usd_stage.html) — documenta abrir stage com configuração de resolução de paths Consulta: 2026-10-04.
