---
id: software.devops.tranche01.000065
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-25.md"
fontes: ["https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/README.md", "https://kubectl.docs.kubernetes.io/references/kustomize/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Gerenciamento de variantes (`development`, `staging`, `production`) com `base` e `overlays`

## Em uma frase
Na subseção `2) Create variants using overlays`, o README oficial explica como gerenciar variantes tradicionais de uma configuração — como `development`, `staging` e `production` — usando **overlays** que modificam uma **base** comum: move-se o trabalho inicial para o subdiretório `someApp/base` (`deployment.yaml`, `kustomization.yaml`, `service.yaml`) e criam-se diretórios irmãos em `someApp/overlays/development` e `someApp/overlays/production`.

## Por que importa
Copiar e colar todos os manifestos Kubernetes em pastas separadas para dev, staging e prod faz com que uma mudança de porta ou novo serviço seja esquecida em um dos ambientes; com uma `base` única e `overlays` enxutos, tudo o que é comum fica em um só lugar e cada ambiente declara apenas suas diferenças.

## Como funciona
Coloque os recursos e customizações compartilhados em `base/` e crie uma subpasta sob `overlays/` para cada variante (`development`, `staging`, `production`), onde cada overlay é apenas mais uma kustomization que referencia `../../base` em `resources:` e aplica seus próprios patches e labels.

## Exemplo
No exemplo do README para o overlay de produção, o `kustomization.yaml` adiciona o label `variant: prod` (com `includeSelectors: true`), referencia `- ../../base` em `resources:` e aplica dois arquivos em `patches:`.

## Limites e trade-offs
O próprio README define o conceito de forma concisa: "An overlay is just another kustomization, referring to the base, and referring to patches to apply to that base."

## Como verificar
Conferi a subseção `2) Create variants using overlays` no README oficial de `kubernetes-sigs/kustomize`.

## Conexões
- [[kustomize-build-and-kubectl-apply-pipeline]] — Veja também: Geração de YAML customizado com `kustomize build` e aplicação em pipe com `kubectl apply -f -`.
- [[kustomize-patches-replica-and-cpu-count-example]] — Veja também: Aplicação declarativa de `patches` em overlays: ajustando réplicas e limites de CPU por ambiente.

## Fontes
- [Kustomize — README oficial](https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/README.md) — README oficial do Kustomize com customização YAML template-free (analogia make/sed), matriz de versões embutidas no kubectl, kustomization.yaml com labels/includeSelectors/configMapGenerator, kustomize build e overlays com patches.; consultado em 2026-10-03.
- [Kustomize — documentação oficial de referência](https://kubectl.docs.kubernetes.io/references/kustomize/) — Documentação oficial de referência e glossário do Kustomize mantida pelo sig-cli do Kubernetes.; consultado em 2026-10-03.
