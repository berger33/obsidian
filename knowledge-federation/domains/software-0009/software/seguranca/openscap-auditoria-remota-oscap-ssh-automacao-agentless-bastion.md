---
id: software.seguranca.tranche15.001427
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-15.md"
fontes: ["https://raw.githubusercontent.com/OpenSCAP/openscap/maint-1.3/README.md", "https://raw.githubusercontent.com/ComplianceAsCode/content/master/README.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Varredura Remota Agentless via SSH com **`oscap-ssh`**: Auditando e Remediando Frotas de Servidores Linux sem Instalar Agentes Permanentes

## Em uma frase
E quando você precisa auditar 200 servidores Linux remotos a partir de uma estação de auditoria ou runner de CI/CD sem manter daemons permanentes rodando nos servidores? Como executar o OpenSCAP remotamente sobre SSH copiando automaticamente o Data Stream e trazendo de volta o relatório HTML e o arquivo ARF para a sua máquina local?

## Por que importa
Com o utilitário oficial **`oscap-ssh`**!

## Como funciona
Quando você executa **`oscap-ssh usuario@servidor 22 xccdf eval ...`**, o script: **(1)** Abre uma conexão SSH segura (suportando variáveis `OSCAP_SSH_OPTS` para especificar chave privada `-i`, `ProxyJump -J` ou certificados do Teleport/FreeIPA!), **(2)** Cria um diretório temporário seguro no servidor remoto e envia via `scp` o arquivo Data Stream `.xml` (e eventual `--tailoring-file`) da sua estação local para lá, **(3)** Executa o `oscap` remoto, **(4)** Baixa de volta os arquivos `--results`, `--results-arf` e `--report` para a sua máquina local e **(5) Limpa todos os arquivos temporários no servidor remoto**!

## Exemplo
```bash
# Executar auditoria CIS remotamente via SSH (oscap-ssh) enviando o Data Stream local e salvando o relatorio HTML e ARF na estacao do auditor
export OSCAP_SSH_OPTS="-i ~/.ssh/id_ed25519_auditoria -o StrictHostKeyChecking=yes"
oscap-ssh root@10.20.30.50 22 xccdf eval \
  --profile xccdf_org.ssgproject.content_profile_cis \
  --results-arf ./arf-srv50.xml \
  --report ./relatorio-srv50.html /usr/share/xml/scap/ssg/content/ssg-rhel9-ds.xml
```

## Limites e trade-offs
Note uma vantagem enorme do **`oscap-ssh`**: o servidor remoto precisa ter apenas o pacote leve **`openscap-scanner`** instalado — você **não precisa instalar nem atualizar o pacote `scap-security-guide` nos 200 servidores remotos**, porque o `oscap-ssh` sempre envia o arquivo Data Stream mais recente diretamente da máquina central do auditor!

## Como verificar
Para executar o `oscap-ssh` com uma conta não-root que possua `sudo` sem senha no servidor remoto, basta passar a flag **`--sudo`** logo no início: `oscap-ssh --sudo auditor@10.20.30.50 22 xccdf eval ...`!

## Conexões
- [[openscap-auditoria-containers-imagens-vms-oscap-podman-oscap-docker]] — Veja também: Auditoria Offline de **Containers (`oscap-podman` / `oscap-docker`)**, Sistemas de Arquivos Montados (**`oscap-chroot`**) e Imagens de VM (**`oscap-vm` `qcow2`**).
- [[openscap-engenharia-regras-complianceascode-yaml-jinja2-templating]] — Veja também: Como Escrever Regras Customizadas no **`ComplianceAsCode/content`**: `rule.yml`, Templates Parametrizados Jinja2 e Compilação Multi-Formato (`XCCDF`, `OVAL`, `Ansible`, `Bash`, `CEL`).
- [[openscap-arquitetura-scap-xccdf-oval-cpe-source-data-stream-oscap]] — Referência cruzada direta com openscap-arquitetura-scap-xccdf-oval-cpe-source-data-stream-oscap.
- [[openscap-auditoria-xccdf-eval-profiles-cis-stig-pci-arf-relatorio-html]] — Referência cruzada direta com openscap-auditoria-xccdf-eval-profiles-cis-stig-pci-arf-relatorio-html.
- [[teleport-acesso-ssh-certificados-openssh-gravacao-sessao-ebpf]] — Referência cruzada direta com teleport-acesso-ssh-certificados-openssh-gravacao-sessao-ebpf.

## Fontes
- [OpenSCAP Official GitHub Repository (`OpenSCAP/openscap` — NIST SCAP 1.3 Certified)](https://raw.githubusercontent.com/OpenSCAP/openscap/maint-1.3/README.md) — repositório oficial do motor e utilitário `oscap` certificado pelo NIST cobrindo avaliação XCCDF, OVAL, DataStreams (`ssg-*-ds.xml`), relatórios ARF/HTML e `oscap-ssh`; consultado em 2026-10-03.
- [ComplianceAsCode (`SCAP Security Guide`) Official Repository (`ComplianceAsCode/content`)](https://raw.githubusercontent.com/ComplianceAsCode/content/master/README.md) — repositório oficial de conteúdo SCAP como código contendo perfis CIS, DISA STIG, PCI-DSS, HIPAA e ANSSI e geração de remediações Ansible, Bash, Ignition e Kickstart; consultado em 2026-10-03.
