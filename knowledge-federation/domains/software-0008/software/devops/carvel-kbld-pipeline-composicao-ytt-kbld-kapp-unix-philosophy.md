---
id: software.devops.tranche16.001530
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-16.md"
fontes: ["https://raw.githubusercontent.com/carvel-dev/kbld/develop/README.md", "https://carvel.dev/kbld/docs/v0.44.x/config/", "https://raw.githubusercontent.com/carvel-dev/kapp/develop/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Carvel kbld: composição Unix em pipeline com `ytt`, `kbld` e `kapp` para entrega contínua

## Em uma frase
Seguindo a filosofia Unix de ferramentas de propósito único da suíte Carvel, o `kbld` atua como o estágio intermediário entre a renderização de templates (`ytt`) e a convergência no cluster (`kapp`), conectando-se via pipes padrão (`stdin`/`stdout`).

## Por que importa
Ferramentas monolíticas acoplam templating, resolução de imagens e aplicação no cluster em um único binário fechado, dificultando substituir apenas o motor de templates ou auditar o manifesto exato que será aplicado.

## Como funciona
No pipeline `ytt -f config/ | kbld -f - -f kbld-config.yml | kapp deploy -a app -f - --yes`, o `ytt` gera os manifestos YAML estruturados na saída padrão; o `kbld` lê da entrada padrão (`-f -`), resolve ou constrói todas as imagens para digests imutáveis, remove seu próprio arquivo `kind: Config` e entrega o YAML puro e imutável para o `kapp` calcular o diff e convergir o cluster.

## Exemplo
```bash
ytt -f config/ -f values-prod.yml \
  | kbld -f - -f kbld.lock.yml \
  | kapp deploy -a billing-service -f - --diff-changes --yes
```

## Limites e trade-offs
Se qualquer etapa do pipeline falhar (por exemplo, um erro de schema no `ytt` ou uma imagem inexistente no `kbld`), o `kapp` recebe uma entrada vazia ou inválida e aborta imediatamente sem alterar os recursos ativos no cluster (especialmente quando `set -o pipefail` está ativo no shell).

## Como verificar
Execute o pipeline com `--diff-run` no final do comando `kapp` em seu ambiente de CI para validar ponta a ponta o template, os digests de imagem e o diff contra o cluster.

## Conexões
- [[carvel-kbld-anotacoes-rastreabilidade-git-build-auditoria]] — Veja também: Carvel kbld: auditoria de supply chain no cluster via anotação `kbld.k14s.io/images`.

## Fontes
- [Carvel kbld GitHub — README.md (Image Building Orchestration, Immutable Digest Resolution & Resource Metadata Annotations)](https://raw.githubusercontent.com/carvel-dev/kbld/develop/README.md) — README oficial do carvel-dev/kbld descrevendo orquestração de builds, resolução de imagens para digests SHA-256 e anotações de metadados; consultado em 2026-10-03.
- [Carvel kbld Official Documentation — Configuration v0.44.x (searchRules, keyMatcher, valueMatcher, updateStrategy, overrides, sources & destinations)](https://carvel.dev/kbld/docs/v0.44.x/config/) — Especificação oficial do objeto Config (kbld.k14s.io/v1alpha1) detalhando searchRules, parse recursivo de YAML/JSON em ConfigMaps, sources, destinations e overrides; consultado em 2026-10-03.
- [Carvel kbld — Official GitHub Repository](https://raw.githubusercontent.com/carvel-dev/kapp/develop/README.md) — Repositório oficial Apache-2.0 do Carvel kbld; consultado em 2026-10-03.
