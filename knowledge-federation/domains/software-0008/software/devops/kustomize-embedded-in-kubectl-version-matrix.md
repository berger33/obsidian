---
id: software.devops.tranche01.000062
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-01.md"
fontes: ["https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/README.md", "https://github.com/kubernetes-sigs/kustomize"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Integração nativa no `kubectl`: histórico de versões embutidas e verificação com `kubectl version --client`

## Em uma frase
A seção `kubectl integration` do README oficial mostra como descobrir a versão do Kustomize embutida em versões recentes do `kubectl` executando `kubectl version --client` (exemplificando com `Client Version: v1.31.0` e `Kustomize Version: v5.4.2`) e documenta a evolução histórica: o fluxo do Kustomize `v2.0.3` foi adicionado ao `kubectl v1.14`, permaneceu congelado em `v2.0.3` da `v1.14` até a `v1.20`, foi atualizado para `v4.0.5` no `kubectl v1.21` e passou a ser atualizado regularmente (chegando a `v5.0.1` no `kubectl v1.27`).

## Por que importa
Diferenças entre a versão do binário `kustomize` standalone instalado na máquina do desenvolvedor e a versão do Kustomize embutida dentro do `kubectl` do runner de CI/CD podem causar divergências de comportamento em campos novos; checar `kubectl version --client` revela imediatamente qual versão do Kustomize está dentro do `kubectl`.

## Como funciona
Execute `kubectl version --client` para auditar a versão do Kustomize embutida no seu `kubectl` ou instale o binário standalone seguindo `https://kubectl.docs.kubernetes.io/installation/kustomize/` quando precisar de uma versão específica independente do ciclo do `kubectl`.

## Exemplo
A tabela oficial do README registra a progressão exata: `< v1.14` (`n/a`), `v1.14-v1.20` (`v2.0.3`), `v1.21` (`v4.0.5`), `v1.22` (`v4.2.0`), `v1.23` (`v4.4.1`), `v1.24` (`v4.5.4`), `v1.25` e `v1.26` (`v4.5.7`), `v1.27` (`v5.0.1`), até o exemplo de saída `v1.31.0` com `v5.4.2`.

## Limites e trade-offs
Sempre que atualizar o `kubectl` em servidores de CI, verifique as notas de lançamento do Kubernetes para conferir se a versão embutida do Kustomize avançou.

## Como verificar
Conferi a seção `kubectl integration` e sua tabela de versões no README oficial de `kubernetes-sigs/kustomize`.

## Conexões
- [[kustomize-what-it-is-make-and-sed-analogy]] — Veja também: Kustomize: customização de YAML bruto e livre de templates com a semântica de `make` e `sed`.
- [[kustomize-base-kustomization-file-anatomy]] — Veja também: Anatomia de um `kustomization.yaml` base: `resources`, `labels` (`includeSelectors`) e `configMapGenerator`.

## Fontes
- [Kustomize — README oficial](https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/README.md) — README oficial do Kustomize com customização YAML template-free (analogia make/sed), matriz de versões embutidas no kubectl, kustomization.yaml com labels/includeSelectors/configMapGenerator, kustomize build e overlays com patches.; consultado em 2026-10-03.
- [Repositório oficial kubernetes-sigs/kustomize](https://github.com/kubernetes-sigs/kustomize) — Repositório oficial do Kustomize no GitHub (sig-cli) com examples/, proposals/ e releases.; consultado em 2026-10-03.
