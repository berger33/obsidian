---
id: software.devops.tranche01.000066
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
fontes: ["https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/README.md", "https://github.com/kubernetes-sigs/kustomize"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Aplicação declarativa de `patches` em overlays: ajustando réplicas e limites de CPU por ambiente

## Em uma frase
O diagrama da subseção `2) Create variants using overlays` no README oficial ilustra exatamente como um overlay altera campos pontuais de um `Deployment` vindo da base por meio da lista `patches:`: o arquivo `replica_count.yaml` declara apenas `apiVersion: apps/v1`, `kind: Deployment`, `metadata: name: myapp` e `spec: replicas: 80`; e o arquivo `cpu_count.yaml` declara a identificação do `Deployment` `myapp` e altera `spec.template.spec.containers[name=myapp].resources.limits` para `memory: "128Mi"` e `cpu: "7000m"`.

## Por que importa
Na base original, o container `myapp` tinha `cpu: "500m"` e nenhuma contagem alta de réplicas; usando pequenos fragmentos YAML de patch (`replica_count.yaml` e `cpu_count.yaml`) no overlay de produção, o operador eleva a escala para 80 réplicas e 7000m de CPU sem duplicar o restante do manifesto do Deployment (portas, seletores, imagem).

## Como funciona
Escreva arquivos de patch focados contendo apenas o cabeçalho de identificação do recurso Kubernetes (`apiVersion`, `kind`, `metadata.name`) e os campos específicos que mudam naquele ambiente, referenciando-os sob `patches:` com `- path: <arquivo.yaml>` no `kustomization.yaml` do overlay.

## Exemplo
Separar `replica_count.yaml` e `cpu_count.yaml` em arquivos distintos dentro do overlay torna imediato entender o propósito de cada ajuste ao listar o diretório do ambiente.

## Limites e trade-offs
Para que o Kustomize case corretamente o patch com o objeto vindo da base e mescle a lista `containers:`, o `metadata.name` do recurso e o `name: myapp` do container no patch precisam coincidir exatamente com os da base.

## Como verificar
Conferi o diagrama de overlay (`kustomization.yaml`, `replica_count.yaml` e `cpu_count.yaml`) no README oficial de `kubernetes-sigs/kustomize`.

## Conexões
- [[kustomize-variants-with-base-and-overlays]] — Veja também: Gerenciamento de variantes (`development`, `staging`, `production`) com `base` e `overlays`.
- [[kustomize-git-workflow-sibling-repos-without-submodules]] — Veja também: Fluxo Git com repositórios irmãos em disco: consumindo bases upstream sem precisar de Git submodules.

## Fontes
- [Kustomize — README oficial](https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/README.md) — README oficial do Kustomize com customização YAML template-free (analogia make/sed), matriz de versões embutidas no kubectl, kustomization.yaml com labels/includeSelectors/configMapGenerator, kustomize build e overlays com patches.; consultado em 2026-10-03.
- [Repositório oficial kubernetes-sigs/kustomize](https://github.com/kubernetes-sigs/kustomize) — Repositório oficial do Kustomize no GitHub (sig-cli) com examples/, proposals/ e releases.; consultado em 2026-10-03.
