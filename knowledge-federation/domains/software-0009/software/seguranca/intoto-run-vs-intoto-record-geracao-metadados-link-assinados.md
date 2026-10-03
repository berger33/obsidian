---
id: software.seguranca.tranche03.000253
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

# in-toto Execução de Etapas (`in-toto-run` vs `in-toto-record start`/`stop`): captura de hashes de `materials`, comando e `products`

## Em uma frase
Para gerar os metadados de evidência (`.link`) durante a execução de cada etapa da cadeia de suprimentos, o in-toto fornece duas ferramentas de CLI documentadas no README oficial: **`in-toto-run`** (para etapas executadas por um único comando atômico) e **`in-toto-record start` / `in-toto-record stop`** (para etapas de múltiplas partes ou edições manuais).

## Por que importa
Em um step de compilação no CI (`go build`), um único comando transforma os fontes no binário; já quando um desenvolvedor edita arquivos em sua IDE ao longo de várias ações antes de comitar, não há um único comando wrapper.

## Como funciona
O **`in-toto-run`** calcula os hashes dos `--materials` antes de rodar o comando, executa o comando, calcula os hashes dos `--products` ao terminar e assina o arquivo `<step-name>.<keyid-prefix>.link`. Já o **`in-toto-record start`** grava um arquivo `.link-unfinished` com os hashes iniciais dos `--materials`, permitindo rodar múltiplos comandos até fechar e assinar com **`in-toto-record stop`**!

## Exemplo
```bash
# Executando o passo 'package' com in-toto-run, registrando o binário de entrada (material) e o tar.gz gerado (product):
in-toto-run \
  --step-name package \
  --materials dist/app-linux-amd64 \
  --products release/app-v1.0.0.tar.gz \
  --signing-key ./ci-packager-key \
  -- tar czf release/app-v1.0.0.tar.gz dist/app-linux-amd64
```

## Limites e trade-offs
Conforme alerta o README oficial, o `in-toto-run` só registra no arquivo `.link` os arquivos explicitamente passados em `--materials` (`-m`) e `--products` (`-p`); especifique sempre os diretórios ou arquivos exatos que as regras do layout exigem.

## Como verificar
Inspecione o arquivo `.link` gerado (em JSON/DSSE) com `jq .` para ver os dicionários `materials`, `products` e `byproducts`.

## Conexões
- [[intoto-artifact-rules-materials-products-match-create-disallow]] — Veja também: in-toto Artifact Rules (`MATCH`, `CREATE`, `MODIFY`, `DELETE`, `ALLOW`, `DISALLOW`, `REQUIRE`): encadeamento criptográfico entre etapas.
- [[intoto-inspections-verificacao-final-in-toto-verify-untar]] — Veja também: in-toto `Inspections` e `in-toto-verify`: desempacotamento e validação criptográfica no momento da instalação pelo cliente.

## Fontes
- [CNCF in-toto GitHub — README.md (Supply Chain Layout, Functionaries, Artifact Rules, in-toto-run, in-toto-record, Inspections & in-toto-verify)](https://raw.githubusercontent.com/in-toto/in-toto/develop/README.md) — README oficial do in-toto/in-toto documentando a estrutura de layouts, regras de encadeamento de materials/products, geração de links e verificação final; consultado em 2026-10-03.
- [CNCF in-toto Attestation Framework GitHub — README.md (Statement v1 Specification, Vetted Predicates, DSSE, SLSA Intersection & Language Bindings)](https://raw.githubusercontent.com/in-toto/attestation/main/README.md) — README oficial do in-toto/attestation descrevendo a especificação do Attestation Framework v1, catálogo de predicados, definições Protobuf e interseção com SLSA; consultado em 2026-10-03.
- [CNCF in-toto — Official GitHub Repository](https://github.com/in-toto/in-toto) — Repositório oficial Apache-2.0 do CNCF in-toto; consultado em 2026-10-03.
