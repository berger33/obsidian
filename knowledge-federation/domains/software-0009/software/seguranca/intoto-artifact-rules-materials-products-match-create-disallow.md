---
id: software.seguranca.tranche03.000252
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

# in-toto Artifact Rules (`MATCH`, `CREATE`, `MODIFY`, `DELETE`, `ALLOW`, `DISALLOW`, `REQUIRE`): encadeamento criptográfico entre etapas

## Em uma frase
Conforme detalhado na seção *Artifact Rules* do README oficial (`in-toto/in-toto`), o coração da segurança de um `layout` do in-toto é a linguagem de **Regras de Artefatos**, que restringe e encadeia os arquivos de entrada (**`materials`**) e os arquivos resultantes (**`products`**) entre etapas consecutivas usando sete verbos: **`MATCH`**, **`CREATE`**, **`DELETE`**, **`MODIFY`**, **`ALLOW`**, **`DISALLOW`** e **`REQUIRE`**.

## Por que importa
Se o passo `clone-repo` baixar o código-fonte `foo.py` com hash `SHA256=AAA`, mas no servidor de compilação um atacante substituir `foo.py` por uma versão maliciosa com hash `SHA256=BBB` antes do passo `build`, sem uma regra de encadeamento entre os dois links a adulteração passaria despercebida!

## Como funciona
Com a regra **`MATCH foo.py WITH PRODUCTS FROM clone-repo`** nos `expected_materials` do passo `build`, o verificador exige que o hash SHA-256 de `foo.py` registrado na entrada do passo `build` seja **idêntico** ao hash registrado na saída do passo `clone-repo`, e uma regra final **`DISALLOW *`** proíbe qualquer arquivo não autorizado!

## Exemplo
```python
# Exemplo de regras encadeando materials e products em um step de Layout do in-toto:
step_build = {
    "name": "build-binary",
    "expected_materials": [
        ["MATCH", "src/*.go", "WITH", "PRODUCTS", "FROM", "vcs-checkout"],
        ["DISALLOW", "*"]
    ],
    "expected_products": [
        ["CREATE", "dist/app-linux-amd64"],
        ["DISALLOW", "*"]
    ]
}
```

## Limites e trade-offs
Atenção à recomendação oficial do README do in-toto: como as *Artifact Rules* por padrão permitem artefatos que não foram explicitamente proibidos, inclua sempre **`["DISALLOW", "*"]`** como a última regra de `expected_materials` e `expected_products` em todas as etapas!

## Como verificar
Verifique no seu `root.layout` que todas as listas de regras de materiais e produtos terminam com `DISALLOW *`.

## Conexões
- [[intoto-arquitetura-cncf-supply-chain-integrity-layout-functionaries-links]] — Veja também: CNCF in-toto: arquitetura de integridade fim-a-fim da cadeia de suprimentos (`Layout`, `Functionaries`, `Steps`, `Links` e `Inspections`).
- [[intoto-run-vs-intoto-record-geracao-metadados-link-assinados]] — Veja também: in-toto Execução de Etapas (`in-toto-run` vs `in-toto-record start`/`stop`): captura de hashes de `materials`, comando e `products`.

## Fontes
- [CNCF in-toto GitHub — README.md (Supply Chain Layout, Functionaries, Artifact Rules, in-toto-run, in-toto-record, Inspections & in-toto-verify)](https://raw.githubusercontent.com/in-toto/in-toto/develop/README.md) — README oficial do in-toto/in-toto documentando a estrutura de layouts, regras de encadeamento de materials/products, geração de links e verificação final; consultado em 2026-10-03.
- [CNCF in-toto Attestation Framework GitHub — README.md (Statement v1 Specification, Vetted Predicates, DSSE, SLSA Intersection & Language Bindings)](https://raw.githubusercontent.com/in-toto/attestation/main/README.md) — README oficial do in-toto/attestation descrevendo a especificação do Attestation Framework v1, catálogo de predicados, definições Protobuf e interseção com SLSA; consultado em 2026-10-03.
- [CNCF in-toto — Official GitHub Repository](https://github.com/in-toto/in-toto) — Repositório oficial Apache-2.0 do CNCF in-toto; consultado em 2026-10-03.
