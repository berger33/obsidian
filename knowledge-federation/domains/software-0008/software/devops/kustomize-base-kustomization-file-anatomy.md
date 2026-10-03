---
id: software.devops.tranche01.000063
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
fontes: ["https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/README.md", "https://kubectl.docs.kubernetes.io/references/kustomize/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Anatomia de um `kustomization.yaml` base: `resources`, `labels` (`includeSelectors`) e `configMapGenerator`

## Em uma frase
Na seção `Usage / 1) Make a kustomization file`, o README oficial mostra um diretório `~/someApp` contendo `deployment.yaml`, `service.yaml` e `kustomization.yaml` com `apiVersion: kustomize.config.k8s.io/v1beta1` e `kind: Kustomization`, declarando três blocos: `labels` (com `includeSelectors: true` e `pairs: app: myapp`), `resources` (listando `deployment.yaml` e `service.yaml`) e `configMapGenerator` (criando o ConfigMap `myapp-map` a partir de `literals: - KEY=value`).

## Por que importa
Em vez de editar manualmente cada arquivo de recurso para injetar rótulos comuns ou escrever um arquivo estático de ConfigMap separado para variáveis simples, o `kustomization.yaml` centraliza a lista de recursos pertencentes à aplicação, propaga labels (incluindo nos seletores quando `includeSelectors: true`) e gera ConfigMaps declarativamente.

## Como funciona
Crie um arquivo `kustomization.yaml` no diretório dos seus manifestos declarando `apiVersion: kustomize.config.k8s.io/v1beta1`, `kind: Kustomization`, a lista de arquivos em `resources:` e as transformações ou geradores desejados (`labels:`, `configMapGenerator:`).

## Exemplo
No diagrama lado a lado do README, o `deployment.yaml` (com container `myapp`, limites `128Mi`/`500m` e `containerPort: 6060`) e o `service.yaml` (porta `6060`) permanecem limpos e legíveis enquanto o `kustomization.yaml` coordena a montagem.

## Limites e trade-offs
Como os arquivos listados em `resources:` não são modificados no disco, se eles vierem de um fork de configuração de terceiros você pode fazer `git rebase` do repositório upstream facilmente para capturar melhorias.

## Como verificar
Conferi a subseção `1) Make a kustomization file` no README oficial de `kubernetes-sigs/kustomize`.

## Conexões
- [[kustomize-embedded-in-kubectl-version-matrix]] — Veja também: Integração nativa no `kubectl`: histórico de versões embutidas e verificação com `kubectl version --client`.
- [[kustomize-build-and-kubectl-apply-pipeline]] — Veja também: Geração de YAML customizado com `kustomize build` e aplicação em pipe com `kubectl apply -f -`.

## Fontes
- [Kustomize — README oficial](https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/README.md) — README oficial do Kustomize com customização YAML template-free (analogia make/sed), matriz de versões embutidas no kubectl, kustomization.yaml com labels/includeSelectors/configMapGenerator, kustomize build e overlays com patches.; consultado em 2026-10-03.
- [Kustomize — documentação oficial de referência](https://kubectl.docs.kubernetes.io/references/kustomize/) — Documentação oficial de referência e glossário do Kustomize mantida pelo sig-cli do Kubernetes.; consultado em 2026-10-03.
