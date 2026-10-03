---
id: software.devops.tranche01.000064
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

# Geração de YAML customizado com `kustomize build` e aplicação em pipe com `kubectl apply -f -`

## Em uma frase
Ao final do passo 1 da seção Usage, o README oficial demonstra os dois comandos fundamentais para consumir um diretório Kustomize: `kustomize build ~/someApp` para emitir o YAML customizado resultante na saída padrão, e `kustomize build ~/someApp | kubectl apply -f -` para aplicar diretamente o resultado em um cluster Kubernetes.

## Por que importa
Poder inspecionar o YAML completo gerado na stdout com `kustomize build <dir>` antes de enviá-lo ao cluster permite revisar diffs exatos em CI/CD, passar a saída por validadores de políticas (como linters de esquemas e segurança) e só então canalizá-la para `kubectl apply -f -`.

## Como funciona
Rode `kustomize build <diretorio>` localmente ou no pipeline de Pull Request para auditar o manifesto final renderizado e use `kustomize build <diretorio> | kubectl apply -f -` (ou a integração nativa do `kubectl`) no momento do deploy.

## Exemplo
O mesmo padrão de comando funciona tanto para um diretório simples (`kustomize build ~/someApp`) quanto para um overlay específico de ambiente (`kustomize build ~/someApp/overlays/production | kubectl apply -f -`).

## Limites e trade-offs
Como `kustomize build` apenas emite o texto YAML editado na saída padrão sem tocar nos arquivos de entrada nem falar com o cluster sozinho, ele é totalmente seguro para rodar offline em qualquer etapa de validação.

## Como verificar
Conferi os passos 1 e 2 da seção Usage no README oficial de `kubernetes-sigs/kustomize`.

## Conexões
- [[kustomize-base-kustomization-file-anatomy]] — Veja também: Anatomia de um `kustomization.yaml` base: `resources`, `labels` (`includeSelectors`) e `configMapGenerator`.
- [[kustomize-variants-with-base-and-overlays]] — Veja também: Gerenciamento de variantes (`development`, `staging`, `production`) com `base` e `overlays`.

## Fontes
- [Kustomize — README oficial](https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/README.md) — README oficial do Kustomize com customização YAML template-free (analogia make/sed), matriz de versões embutidas no kubectl, kustomization.yaml com labels/includeSelectors/configMapGenerator, kustomize build e overlays com patches.; consultado em 2026-10-03.
- [Repositório oficial kubernetes-sigs/kustomize](https://github.com/kubernetes-sigs/kustomize) — Repositório oficial do Kustomize no GitHub (sig-cli) com examples/, proposals/ e releases.; consultado em 2026-10-03.
