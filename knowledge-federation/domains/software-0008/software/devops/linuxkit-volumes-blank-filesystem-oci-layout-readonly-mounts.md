---
id: software.devops.tranche20.001904
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

# LinuxKit Seção `volumes`: criação em tempo de build de volumes em branco, `filesystem` populado por imagem e `format: oci`

## Em uma frase
A seção **`volumes:`** do LinuxKit permite declarar volumes nomeados criados em tempo de build que podem ser compartilhados e montados por containers em `onboot`, `services` e `onshutdown`, suportando três formatos: diretório em branco, **`format: filesystem`** (populado pelo conteúdo de uma imagem OCI) e **`format: oci`** (layout OCI v1 de imagens).

## Por que importa
Quando múltiplos containers de sistema precisam compartilhar um conjunto de binários auxiliares, certificados ou imagens OCI pré-carregadas para ambientes *air-gapped* sem duplicar camadas dentro de cada container, volumes nomeados resolvem o acoplamento em tempo de build.

## Como funciona
Cada entrada em `volumes:` define `name` (apenas caracteres alfanuméricos minúsculos, hífens e underscores), `image` opcional, `format` (`filesystem` ou `oci`), `platforms` e `readonly` (`true` ou `false`). Se um volume for declarado com `readonly: true`, qualquer tentativa de montá-lo como leitura-escrita (`rw`) em um container gera erro imediato durante o `linuxkit build`.

## Exemplo
```yaml
volumes:
  - name: shared-tools
    image: alpine:3.20
    format: filesystem
    readonly: true
  - name: airgap-images
    image: busybox:latest
    format: oci
    readonly: true
```

## Limites e trade-offs
Se um volume for declarado como `readonly: false` (o padrão), ele ainda pode ser montado individualmente como `ro` em containers que precisem apenas de acesso de leitura e `rw` no container responsável por atualizá-lo.

## Como verificar
Teste a criação dos volumes rodando `linuxkit build` e valide que referências a volumes `readonly: true` com permissão de escrita são barradas em tempo de compilação.

## Conexões
- [[linuxkit-alocacao-automatica-uid-gid-isolamento-containers-files]] — Veja também: LinuxKit Isolamento de Identidades: alocação automática de `uid` e `gid` por nome de container entre `services` e `files`.
- [[linuxkit-formatos-saida-build-iso-efi-raw-bios-qcow2-vhd-aws-gcp]] — Veja também: LinuxKit Formatos de Saída (`linuxkit build --format`): geração de imagens para `iso-efi`, `raw-bios`, `qcow2`, `vhd`, AWS, GCP e Raspberry Pi.

## Fontes
- [LinuxKit GitHub — README.md (Toolkit for Building Secure, Portable and Lean Operating Systems for Containers)](https://raw.githubusercontent.com/linuxkit/linuxkit/master/docs/yaml.md) — README oficial do linuxkit/linuxkit apresentando a arquitetura de imagens de SO imutáveis, formatos de saída, plataformas de execução e ferramentas; consultado em 2026-10-03.
- [LinuxKit Official Documentation — YAML Specification (docs/yaml.md: kernel, init, volumes, onboot, onshutdown, services & files)](https://raw.githubusercontent.com/linuxkit/linuxkit/master/README.md) — Especificação oficial YAML do LinuxKit detalhando a ordem de inicialização, alocação simbólica de uid/gid, volumes OCI e configuração runtime; consultado em 2026-10-03.
- [LinuxKit — Official GitHub Repository](https://github.com/linuxkit/linuxkit) — Repositório oficial Apache-2.0 do LinuxKit; consultado em 2026-10-03.
