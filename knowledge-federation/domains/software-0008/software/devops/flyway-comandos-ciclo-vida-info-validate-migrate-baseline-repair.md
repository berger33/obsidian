---
id: software.devops.tranche08.000756
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-08.md"
fontes: ["https://raw.githubusercontent.com/flyway/flyway/main/README.md", "https://documentation.red-gate.com/flyway/getting-started-with-flyway", "https://github.com/flyway/flyway"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Redgate Flyway: comandos fundamentais do ciclo de vida (migrate, info, validate, baseline, repair e clean)

## Em uma frase
A operação do Flyway apoia-se em seis comandos principais: `migrate` (aplica pendentes), `info` (detalha status), `validate` (verifica checksums e histórico), `baseline` (adota bancos existentes), `repair` (corrige histórico/checksums) e `clean` (apaga objetos em desenvolvimento).

## Por que importa
Adotar o Flyway em um banco de dados legado que já está em produção há anos exige marcar um ponto de partida (`baseline`) sem tentar recriar tabelas que já existem; da mesma forma, saber validar integridade em CI (`validate`) e bloquear `clean` em produção evita perda catastrófica de dados. A documentação oficial `Getting started with Flyway` detalha cada um desses comandos.

## Como funciona
(1) **`info`**: imprime o estado detalhado e a versão de todas as migrações (aplicadas, pendentes, fora de ordem ou falhas); (2) **`validate`**: verifica se as migrações aplicadas no banco batem em checksum e presença com as disponíveis localmente (executado por padrão antes do `migrate`); (3) **`migrate`**: aplica todas as migrações pendentes até a versão mais recente (ou até `-target`); (4) **`baseline`**: cria a tabela `flyway_schema_history` em um banco não-vazio existente e insere um marcador `« Flyway Baseline »` (ex.: na versão `1`), fazendo o Flyway ignorar scripts `<= baselineVersion` e aplicar apenas versões posteriores; (5) **`repair`**: remove entradas de migrações falhas (em bancos sem DDL transacional) e realinha checksums; e (6) **`clean`**: remove todos os objetos nos schemas configurados (útil em testes locais, mas deve manter `cleanDisabled=true` em produção).

## Exemplo
```bash
# Adotar um banco de dados legado existente na versão 1.0 com baseline e verificar com info
flyway -url="jdbc:postgresql://localhost:5432/legacydb" -user="postgres" -baselineVersion="1.0" baseline
flyway -url="jdbc:postgresql://localhost:5432/legacydb" -user="postgres" info
```

## Limites e trade-offs
O comando `flyway clean` apaga **todas** as tabelas, views, procedures e dados dos schemas gerenciados pelo Flyway; por segurança, versões modernas do Flyway já vêm com `flyway.cleanDisabled=true` por padrão, e essa proteção jamais deve ser desativada (`cleanDisabled=false`) em ambientes de homologação compartilhada ou produção.

## Como verificar
Em pipelines de Pull Request, execute `flyway validate` e `flyway info` para garantir que nenhum script antigo foi adulterado antes de autorizar o `flyway migrate`.

## Conexões
- [[flyway-nomenclatura-migracoes-versionadas-repetiveis-undo]] — Veja também: Redgate Flyway: convenção de nomenclatura de migrações Versionadas (V), Repetíveis (R) e Undo (U).
- [[flyway-migracoes-java-jdbc-placeholders-callbacks]] — Veja também: Redgate Flyway: migrações escritas em Java (BaseJavaMigration), substituição de Placeholders e Callbacks.
- [[flyway-migracoes-banco-dados-schema-history-versionamento]] — Referência cruzada direta com flyway-migracoes-banco-dados-schema-history-versionamento.

## Fontes
- [Redgate Flyway GitHub — README.md (How Flyway Works, 5 Execution Modes, Schema Model & 50+ Supported Databases)](https://raw.githubusercontent.com/flyway/flyway/main/README.md) — README oficial do Flyway (Apache-2.0) explicando o funcionamento da tabela flyway_schema_history, migrações SQL e Java, captura de schema model em disco e matriz de mais de 50 bancos suportados; consultado em 2026-10-03.
- [Redgate Flyway Official Documentation — Getting Started with Flyway](https://documentation.red-gate.com/flyway/getting-started-with-flyway) — Documentação oficial da Redgate para configuração, convenções de nomenclatura (V, R, U) e comandos de ciclo de vida do Flyway; consultado em 2026-10-03.
- [Redgate Flyway — Official GitHub Repository](https://github.com/flyway/flyway) — Repositório oficial Apache-2.0 do Redgate Flyway; consultado em 2026-10-03.
