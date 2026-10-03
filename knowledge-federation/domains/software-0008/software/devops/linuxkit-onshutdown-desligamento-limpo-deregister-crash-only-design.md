---
id: software.devops.tranche20.001909
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-20.md"
fontes: ["https://raw.githubusercontent.com/linuxkit/linuxkit/master/docs/yaml.md", "https://raw.githubusercontent.com/linuxkit/linuxkit/master/README.md", "https://github.com/linuxkit/linuxkit"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# LinuxKit `onshutdown` e *Crash-Only Software*: execução de containers de desligamento limpo e limites operacionais

## Em uma frase
A seção **`onshutdown:`** do manifesto YAML do LinuxKit define uma lista de imagens de container executadas durante um desligamento limpo (*clean shutdown*) do sistema operacional, permitindo desregistrar o nó de um balanceador de carga, drenar sessões ou sincronizar estado final.

## Por que importa
Quando um nó de auto-scaling grupo na nuvem recebe um sinal ACPI de encerramento, desregistrar proativamente o nó de um cluster Consul/Kubernetes ou service discovery evita que clientes recebam erros de conexão durante o intervalo de timeout de health check.

## Como funciona
Entretanto, a documentação oficial (`docs/yaml.md`) alerta enfaticamente: você **jamais deve depender** exclusivamente da execução de `onshutdown` para manter a integridade do seu sistema, pois máquinas físicas e VMs podem sofrer queda de energia ou terminação abrupta sem tempo de rodar scripts de parada. Projete os serviços sob a filosofia *crash-only* e use `onshutdown` apenas como otimização graciosa.

## Exemplo
```yaml
onshutdown:
  - name: deregister-node
    image: alpine:3.20
    command: ["/bin/sh", "-c", " echo 'Drenando nó antes do poweroff...' "]
```

## Limites e trade-offs
Conforme recomendado pelo guia oficial do LinuxKit, sempre que adicionar um container em `onshutdown`, teste o comportamento do seu cluster tanto no cenário em que `onshutdown` roda até o fim quanto no cenário de desligamento abrupto (`kill -9` do hipervisor).

## Como verificar
Inicie uma imagem com `linuxkit run`, acione um desligamento ACPI gracioso e observe nos logs do console serial a execução do container listado em `onshutdown`.

## Conexões
- [[linuxkit-armazenamento-persistente-format-mount-extend-var-lib-docker]] — Veja também: LinuxKit Armazenamento Persistente: particionamento e montagem automática no boot com pacotes `format`, `extend` e `mount`.
- [[linuxkit-cache-local-oci-rtf-regression-test-framework]] — Veja também: LinuxKit Image Cache e Testes de Regressão (`rtf`): cache local de imagens OCI e automação de testes de SO.

## Fontes
- [LinuxKit GitHub — README.md (Toolkit for Building Secure, Portable and Lean Operating Systems for Containers)](https://raw.githubusercontent.com/linuxkit/linuxkit/master/docs/yaml.md) — README oficial do linuxkit/linuxkit apresentando a arquitetura de imagens de SO imutáveis, formatos de saída, plataformas de execução e ferramentas; consultado em 2026-10-03.
- [LinuxKit Official Documentation — YAML Specification (docs/yaml.md: kernel, init, volumes, onboot, onshutdown, services & files)](https://raw.githubusercontent.com/linuxkit/linuxkit/master/README.md) — Especificação oficial YAML do LinuxKit detalhando a ordem de inicialização, alocação simbólica de uid/gid, volumes OCI e configuração runtime; consultado em 2026-10-03.
- [LinuxKit — Official GitHub Repository](https://github.com/linuxkit/linuxkit) — Repositório oficial Apache-2.0 do LinuxKit; consultado em 2026-10-03.
