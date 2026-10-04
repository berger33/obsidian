---
id: software.devops.tranche20.001908
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

# LinuxKit Armazenamento Persistente: particionamento e montagem automática no boot com pacotes `format`, `extend` e `mount`

## Em uma frase
Embora o rootfs de uma imagem LinuxKit seja efêmero em memória (initramfs/squashfs), nós de produção que executam `containerd`, Docker ou bancos de dados anexam discos persistentes durante a fase **`onboot`** encadeando os pacotes oficiais **`linuxkit/format`**, **`linuxkit/extend`** e **`linuxkit/mount`**.

## Por que importa
Quando uma VM LinuxKit sobe pela primeira vez com um volume EBS/Persistent Disk bruto anexado (ou quando o volume é expandido na nuvem), o sistema precisa formatar o disco apenas se ele ainda não tiver filesystem, redimensionar a partição se o disco cresceu e montá-lo em `/var/lib/containerd` antes de os serviços iniciarem.

## Como funciona
Declarados sequencialmente em `onboot:`, 1) `linuxkit/format` detecta e formata discos brutos (ex.: `ext4` ou `xfs`) preservando dados caso já estejam formatados; 2) `linuxkit/extend` expande o sistema de arquivos para ocupar 100% do bloco subjacente; e 3) `linuxkit/mount` monta a partição em `/var/lib/docker` ou `/var/lib/containerd` antes de a seção `services:` iniciar.

## Exemplo
```yaml
onboot:
  - name: format
    image: linuxkit/format:v1.0.0
  - name: mount
    image: linuxkit/mount:v1.0.0
    command: ["/usr/bin/mountie", "/var/lib/containerd"]
```

## Limites e trade-offs
Como `onboot` executa os containers estritamente um após o outro e aguarda o término de cada um, `mount` só roda depois que `format` concluiu com sucesso, e os `services` só iniciam com `/var/lib/containerd` já montado em disco.

## Como verificar
Teste a sequência `format` -> `mount` passando `-disk file=data.img,size=2G` para `linuxkit run` e verifique que os dados em `/var/lib/containerd` persistem após reiniciar a VM.

## Conexões
- [[linuxkit-pkg-construcao-pacotes-sistema-oci-reproducible-builds]] — Veja também: LinuxKit Packages (`linuxkit pkg`): construção reprodutível e multi-arquitetura de pacotes de sistema em containers.
- [[linuxkit-onshutdown-desligamento-limpo-deregister-crash-only-design]] — Veja também: LinuxKit `onshutdown` e *Crash-Only Software*: execução de containers de desligamento limpo e limites operacionais.

## Fontes
- [LinuxKit GitHub — README.md (Toolkit for Building Secure, Portable and Lean Operating Systems for Containers)](https://raw.githubusercontent.com/linuxkit/linuxkit/master/README.md) — README oficial do linuxkit/linuxkit apresentando a arquitetura de imagens de SO imutáveis, formatos de saída, plataformas de execução e ferramentas; consultado em 2026-10-03.
- [LinuxKit Official Documentation — YAML Specification (docs/yaml.md: kernel, init, volumes, onboot, onshutdown, services & files)](https://raw.githubusercontent.com/linuxkit/linuxkit/master/docs/yaml.md) — Especificação oficial YAML do LinuxKit detalhando a ordem de inicialização, alocação simbólica de uid/gid, volumes OCI e configuração runtime; consultado em 2026-10-03.
- [LinuxKit — Official GitHub Repository](https://github.com/linuxkit/linuxkit) — Repositório oficial Apache-2.0 do LinuxKit; consultado em 2026-10-03.
