---
id: software.testes.tranche20.001417
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
fontes: ["https://assertj.github.io/doc/", "https://github.com/assertj/assertj"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# AssertJ: usar os módulos complementares

## Em uma frase
Projetos complementares oferecem asserções para tipos de bancos de dados relacionais, coleções de bibliotecas conhecidas e outras estruturas específicas.

## Por que importa
Módulos cobrem domínios que o núcleo deixa de fora, mantendo o mesmo estilo de verificação em camadas especializadas.

## Como funciona
Adote apenas o módulo necessário ao projeto, verifique a versão compatível e prefira as asserções especializadas ao invés de conversões manuais.

## Exemplo
Um teste de consulta pode verificar a tabela resultante com asserções próprias de banco, incluindo colunas e linhas.

## Limites e trade-offs
Módulos não mantidos acumulam incompatibilidades, e misturar asserções de módulos com conversões manuais confunde a leitura.

## Como verificar
Compare o mesmo resultado usando asserções do módulo e código manual e avalie qual versão comunica melhor a falha.

## Conexões
- [[assertj-recursive-and-fields]] — Veja também: AssertJ: comparar campos e estruturas.
- [[assertj-limits-and-practices]] — Veja também: AssertJ: reconhecer limites e boas práticas.

## Fontes
- [AssertJ — Documentação](https://assertj.github.io/doc/) — asserções fluentes, coleções, descrições, asserções suaves e próprias; consultado em 2026-10-03.
- [AssertJ — repositório oficial](https://github.com/assertj/assertj) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
