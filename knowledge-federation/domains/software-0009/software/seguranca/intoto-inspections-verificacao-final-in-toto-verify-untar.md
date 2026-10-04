---
id: software.seguranca.tranche03.000254
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

# in-toto `Inspections` e `in-toto-verify`: desempacotamento e validação criptográfica no momento da instalação pelo cliente

## Em uma frase
Na especificação de um `layout` do in-toto, além dos `steps` (executados pelos *functionaries* durante a produção do software), existe a seção **`inspections`**: comandos executados **pelo próprio verificador (`in-toto-verify`) no momento da verificação final do produto**!

## Por que importa
O consumidor final recebe um pacote fechado `app-v1.0.0.tar.gz`, mas o passo `build` produziu `dist/app-linux-amd64` antes de ser compactado; como o verificador pode comprovar que o binário dentro do `.tar.gz` recebido corresponde exatamente ao produto do passo `build`?

## Como funciona
Declarando uma **`inspection`** chamada `untar` que executa `tar xzf app-v1.0.0.tar.gz` e possui a regra **`MATCH dist/app-linux-amd64 WITH PRODUCTS FROM build-binary`**, o comando `in-toto-verify` extrai o pacote e confere criptograficamente cada arquivo extraído contra os `.link` assinados nas etapas anteriores!

## Exemplo
```bash
# Verificando a integridade completa do produto final contra o root.layout e as chaves públicas dos donos do projeto:
in-toto-verify \
  --layout root.layout \
  --verification-keys owner-alice.pub owner-bob.pub \
  --link-dir ./metadata-links/
```

## Limites e trade-offs
O `in-toto-verify` retorna código de saída **`0`** apenas se: 1) as assinaturas do `root.layout` forem válidas; 2) a data `expires` do layout não tiver vencido; 3) todos os steps tiverem `.link` assinados pelos functionaries autorizados; e 4) todas as regras de `steps` e `inspections` passarem sem violação!

## Como verificar
Execute `in-toto-verify` em um pipeline de deploy antes de promover qualquer artefato para produção.

## Conexões
- [[intoto-run-vs-intoto-record-geracao-metadados-link-assinados]] — Veja também: in-toto Execução de Etapas (`in-toto-run` vs `in-toto-record start`/`stop`): captura de hashes de `materials`, comando e `products`.
- [[intoto-attestation-framework-v1-statement-subject-predicate-dsse]] — Veja também: in-toto Attestation Framework (`v1`): arquitetura das camadas `Envelope (DSSE)`, `Statement`, `subject` e `predicate`.

## Fontes
- [CNCF in-toto GitHub — README.md (Supply Chain Layout, Functionaries, Artifact Rules, in-toto-run, in-toto-record, Inspections & in-toto-verify)](https://raw.githubusercontent.com/in-toto/in-toto/develop/README.md) — README oficial do in-toto/in-toto documentando a estrutura de layouts, regras de encadeamento de materials/products, geração de links e verificação final; consultado em 2026-10-03.
- [CNCF in-toto Attestation Framework GitHub — README.md (Statement v1 Specification, Vetted Predicates, DSSE, SLSA Intersection & Language Bindings)](https://raw.githubusercontent.com/in-toto/attestation/main/README.md) — README oficial do in-toto/attestation descrevendo a especificação do Attestation Framework v1, catálogo de predicados, definições Protobuf e interseção com SLSA; consultado em 2026-10-03.
- [CNCF in-toto — Official GitHub Repository](https://github.com/in-toto/in-toto) — Repositório oficial Apache-2.0 do CNCF in-toto; consultado em 2026-10-03.
