---
id: software.devops.tranche04.000375
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/cri-o/cri-o/main/README.md", "https://cri-o.github.io/cri-o", "https://github.com/cri-o/cri-o"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Inspeção de runtime com crio status e API HTTP sobre socket Unix /var/run/crio/crio.sock

## Em uma frase
Além da API gRPC padrão que atende à CRI do Kubernetes, o CRI-O expõe uma API HTTP adicional sobre o socket Unix `/var/run/crio/crio.sock` e o subcomando dedicado **`crio status`** (`crio status info`, `crio status config`, `crio status containers`) para recuperar informações de diagnóstico do runtime. Os endpoints HTTP suportados incluem `/info` (JSON com `storage_driver`, `storage_root`, `cgroup_driver`, `default_id_mappings`), `/containers/:id` (JSON com nome, PID e imagem do contêiner), `/config` (configuração TOML completa), `/pause/:id`, `/unpause/:id`, `/debug/goroutines` (stacks de goroutines em `text/plain`) e `/debug/heap` (heap dump).

## Por que importa
Quando um nó Kubernetes apresenta lentidão ou suspeita de vazamento de memória/travamento no runtime de contêiner, consultar `/debug/goroutines`, `/debug/heap` e `/info` via `crio status` ou `curl --unix-socket /var/run/crio/crio.sock` permite diagnosticar o estado interno do daemon sem reiniciá-lo.

## Como funciona
Use `sudo crio status info` e `sudo crio status config` nos scripts de diagnóstico de nós ou consulte `sudo curl -v --unix-socket /var/run/crio/crio.sock http://localhost/info | jq` durante investigações de suporte.

## Exemplo
Durante a investigação de um nó `NotReady`, o SRE executa `sudo crio status info` e coleta a pilha de goroutines em `/debug/goroutines` pelo socket `/var/run/crio/crio.sock` para identificar qual operação de armazenamento estava bloqueada.

## Limites e trade-offs
Observe o alerta explícito do README oficial: a API HTTP de status do CRI-O **não é considerada estável** e casos de uso de produção não devem depender dela programaticamente (use-a apenas para diagnóstico e troubleshooting).

## Como verificar
Execute `sudo crio status info` em um nó com CRI-O e confirme a exibição de `cgroup driver`, `storage driver`, `storage root` e dos mapeamentos padrão de UID/GID.

## Conexões
- [[crio-configuration-files-crio-conf-policy-registries-and-storage]] — Veja também: Arquivos de configuração do CRI-O: crio.conf, policy.json, registries.conf e storage.conf.
- [[crio-signature-verification-policy-json-enforcement]] — Veja também: Verificação nativa de assinaturas de imagem no nó Kubernetes com policy.json no CRI-O.

## Fontes
- [CRI-O GitHub — README.md (Kubernetes Compatibility Matrix, Scope, Config & HTTP Status API)](https://raw.githubusercontent.com/cri-o/cri-o/main/README.md) — README oficial do CRI-O detalhando alinhamento de versões 1.x.y e política de version skew n-2 com o Kubernetes, escopo estrito de implementação da CRI para o Kubelet, bibliotecas OCI (runc, container-libs/image, container-libs/storage, CNI), arquivos crio.conf, policy.json, registries.conf, storage.conf e API de status via crio status e socket /var/run/crio/crio.sock.; consultado em 2026-10-03.
- [CRI-O — Official Release Notes & Documentation Portal](https://cri-o.github.io/cri-o) — Portal oficial de notas de versão e relatórios de dependências do CRI-O mantido pelos desenvolvedores do projeto.; consultado em 2026-10-03.
- [CRI-O — Official GitHub Repository](https://github.com/cri-o/cri-o) — Repositório oficial Apache-2.0 do CRI-O na CNCF.; consultado em 2026-10-03.
