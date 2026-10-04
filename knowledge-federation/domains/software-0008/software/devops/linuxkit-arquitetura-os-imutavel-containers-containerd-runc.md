---
id: software.devops.tranche20.001901
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
fontes: ["https://raw.githubusercontent.com/linuxkit/linuxkit/master/README.md", "https://raw.githubusercontent.com/linuxkit/linuxkit/master/docs/yaml.md", "https://github.com/linuxkit/linuxkit"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# LinuxKit: arquitetura de distribuições Linux mínimas e imutáveis construídas com containers sobre `containerd` e `runc`

## Em uma frase
O **LinuxKit** é um toolkit open-source para construir distribuições Linux customizadas, mínimas, stateless e imutáveis para arquiteturas `x86_64`, `arm64` e `s390x`, onde todos os componentes do sistema operacional são empacotados como imagens OCI/Docker e executados como containers de sistema sobre `containerd` e `runc`.

## Por que importa
Sistemas operacionais de propósito geral tradicionais acumulam centenas de pacotes, gerenciadores de pacotes mutáveis e serviços desnecessários nos worker nodes, ampliando a superfície de ataque a CVEs e causando *configuration drift* entre servidores de produção.

## Como funciona
No LinuxKit, a infraestrutura imutável é aplicada à própria construção da distribuição Linux: um manifesto declarativo YAML (`linuxkit.yml`) especifica uma imagem de `kernel`, um sistema `init` base desempacotado no rootfs (contendo `init`, `containerd` e `runc`), containers sequenciais de inicialização (`onboot`) e containers de longa duração (`services`). O comando `linuxkit build` baixa e monta todos os componentes em uma imagem de disco ou ISO auto-contida e reprodutível.

## Exemplo
```bash
# Construindo uma imagem LinuxKit imutável e executando-a localmente com linuxkit run:
linuxkit build linuxkit.yml
linuxkit run linuxkit
```

## Limites e trade-offs
Embora o sistema raiz gerado pelo LinuxKit seja completamente *stateless* e somente-leitura por padrão (garantindo que cada reboot restaure um estado limpo idêntico), discos de armazenamento persistente podem ser montados explicitamente nos containers que necessitam reter estado.

## Como verificar
Execute `linuxkit build linuxkit.yml` e verifique os artefatos de boot gerados no diretório de trabalho antes de inicializar a VM.

## Conexões
- [[linuxkit-manifesto-yaml-ordem-secoes-kernel-init-onboot-services]] — Veja também: LinuxKit Manifesto YAML (`docs/yaml.md`): ordem de processamento de `kernel`, `init`, `volumes`, `onboot`, `onshutdown`, `services` e `files`.

## Fontes
- [LinuxKit GitHub — README.md (Toolkit for Building Secure, Portable and Lean Operating Systems for Containers)](https://raw.githubusercontent.com/linuxkit/linuxkit/master/README.md) — README oficial do linuxkit/linuxkit apresentando a arquitetura de imagens de SO imutáveis, formatos de saída, plataformas de execução e ferramentas; consultado em 2026-10-03.
- [LinuxKit Official Documentation — YAML Specification (docs/yaml.md: kernel, init, volumes, onboot, onshutdown, services & files)](https://raw.githubusercontent.com/linuxkit/linuxkit/master/docs/yaml.md) — Especificação oficial YAML do LinuxKit detalhando a ordem de inicialização, alocação simbólica de uid/gid, volumes OCI e configuração runtime; consultado em 2026-10-03.
- [LinuxKit — Official GitHub Repository](https://github.com/linuxkit/linuxkit) — Repositório oficial Apache-2.0 do LinuxKit; consultado em 2026-10-03.
