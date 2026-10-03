---
id: software.seguranca.tranche03.000251
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-03.md"
fontes: ["https://raw.githubusercontent.com/in-toto/in-toto/develop/README.md", "https://raw.githubusercontent.com/in-toto/attestation/main/README.md", "https://github.com/in-toto/in-toto"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# CNCF in-toto: arquitetura de integridade fim-a-fim da cadeia de suprimentos (`Layout`, `Functionaries`, `Steps`, `Links` e `Inspections`)

## Em uma frase
Conforme documentado no README oficial (`in-toto/in-toto`, projeto Incubating da CNCF licenciado sob Apache 2.0), o **in-toto** é um framework criptográfico projetado para proteger a **integridade de toda a cadeia de suprimentos de software**, verificando que cada etapa da pipeline foi executada apenas por pessoal/sistemas autorizados e que os artefatos não foram adulterados em trânsito entre as etapas.

## Por que importa
Assinar apenas o binário ou pacote final na última etapa do release não prova que o código-fonte veio realmente do Git autorizado, nem que os testes de segurança foram executados ou que o servidor de build não injetou um backdoor antes da assinatura final.

## Como funciona
No in-toto: 1) o **Project Owner** cria e assina um **`root.layout`** definindo a sequência de **`steps`**, as chaves públicas dos **`functionaries`** autorizados a executar cada step e as regras de artefatos; 2) cada functionary executa sua tarefa gerando um arquivo de metadados assinado (**`<step>.<keyid>.link`**) que registra os hashes dos arquivos de entrada (**`materials`**) e saída (**`products`**); e 3) o consumidor valida toda a cadeia com **`in-toto-verify`**!

## Exemplo
```bash
# Instalando o framework in-toto e verificando os utilitários de linha de comando disponíveis:
pip install in-toto
in-toto-run --version
in-toto-verify --version
```

## Limites e trade-offs
O modelo do in-toto separa claramente **política** (o `root.layout`, assinado offline pelos donos do projeto) de **evidência de execução** (os arquivos `.link`, assinados pelos passos da pipeline/desenvolvedores).

## Como verificar
Execute `in-toto-verify --help` para inspecionar os parâmetros de verificação de layout e chaves públicas.

## Conexões
- [[intoto-artifact-rules-materials-products-match-create-disallow]] — Veja também: in-toto Artifact Rules (`MATCH`, `CREATE`, `MODIFY`, `DELETE`, `ALLOW`, `DISALLOW`, `REQUIRE`): encadeamento criptográfico entre etapas.

## Fontes
- [CNCF in-toto GitHub — README.md (Supply Chain Layout, Functionaries, Artifact Rules, in-toto-run, in-toto-record, Inspections & in-toto-verify)](https://raw.githubusercontent.com/in-toto/in-toto/develop/README.md) — README oficial do in-toto/in-toto documentando a estrutura de layouts, regras de encadeamento de materials/products, geração de links e verificação final; consultado em 2026-10-03.
- [CNCF in-toto Attestation Framework GitHub — README.md (Statement v1 Specification, Vetted Predicates, DSSE, SLSA Intersection & Language Bindings)](https://raw.githubusercontent.com/in-toto/attestation/main/README.md) — README oficial do in-toto/attestation descrevendo a especificação do Attestation Framework v1, catálogo de predicados, definições Protobuf e interseção com SLSA; consultado em 2026-10-03.
- [CNCF in-toto — Official GitHub Repository](https://github.com/in-toto/in-toto) — Repositório oficial Apache-2.0 do CNCF in-toto; consultado em 2026-10-03.
