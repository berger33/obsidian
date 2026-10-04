---
id: software.seguranca.tranche12.001129
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-12.md"
fontes: ["https://raw.githubusercontent.com/mitre/caldera/master/README.md", "https://caldera.readthedocs.io/en/latest/Learning-the-terminology.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Hardening e Segurança Operacional de uma Implantação do **MITRE Caldera**: `conf/local.yml`, Plugin **`ssl`**, **`saml`** e Isolamento de Rede

## Em uma frase
Como o próprio servidor do **MITRE Caldera** é um servidor de Command-and-Control (C2) com agentes capazes de executar comandos arbitrários nos hosts conectados, **um servidor Caldera mal configurado (rodando com `--insecure`, credenciais padrão `red`/`admin` e exposto na rede) representa um risco crítico de comprometimento da infraestrutura**!

## Por que importa
Para implantar o Caldera com segurança em um ambiente corporativo de Purple Team, siga rigorosamente as recomendações oficiais de segurança: **(1)** Nunca use `conf/default.yml` em produção — gere e proteja o **`conf/local.yml`** com chaves de criptografia fortes (`encryption_key`, `crypt_salt`) e senhas/API keys aleatórias longas para os usuários `red` e `blue`; **(2)** Habilite o plugin **`ssl`** (ou um Reverse Proxy TLS com mTLS/autenticação forte e o plugin **`saml`**) para criptografar tanto a interface Web quanto o tráfego de beacon dos agentes; e **(3)** Restrinja por firewall (`nftables` / Security Groups) quem pode acessar a porta `8888`!

## Como funciona
Lembre-se também de proteger o diretório `data/` (que armazena artefatos exfiltrados e estados de operações criptografados com a `encryption_key` do `local.yml`) com permissões `0700` no sistema de arquivos do host.

## Exemplo
```bash
# Verificar permissoes restritas do arquivo conf/local.yml e validar se os plugins ssl e stockpile estao ativos na configuracao local
chmod 600 ./caldera/conf/local.yml
grep -E "^(host|port|encryption_key|crypt_salt):" ./caldera/conf/local.yml
```

## Limites e trade-offs
Nunca deixe agentes **Sandcat** instalados permanentemente em servidores de produção após o término de uma janela de testes: desinstale os agentes e rotacione a `api_key_red` e `api_key_blue` periodicamente.

## Como verificar
Em contêineres Docker, monte o arquivo `conf/local.yml` e o diretório `data/` em volumes persistentes criptografados para evitar que o reinício do container regenere chaves e invalide sessões.

## Conexões
- [[caldera-movimentacao-lateral-descoberta-fatos-credenciais-smb-ssh]] — Veja também: Emulação Automática de **Movimentação Lateral** no Caldera: Encadeando Descoberta de Sub-rede, Extração de Credenciais e Pivô SMB/SSH/WinRM.
- [[caldera-desenvolvimento-plugins-customizados-skeleton-abilities-parsers]] — Veja também: Extensibilidade do Caldera: Criando **Plugins Customizados (`mitre/skeleton`)**, Novos **Parsers de Fatos** e **Planners** Sob Medida.
- [[caldera-arquitetura-plataforma-emulacao-adversarios-c2-plugins]] — Referência cruzada direta com caldera-arquitetura-plataforma-emulacao-adversarios-c2-plugins.
- [[caldera-agentes-sandcat-manx-ragdoll-c2-contacts-paw]] — Referência cruzada direta com caldera-agentes-sandcat-manx-ragdoll-c2-contacts-paw.
- [[nftables-arquitetura-firewall-kernel-linux-netfilter-tabelas-inet]] — Referência cruzada direta com nftables-arquitetura-firewall-kernel-linux-netfilter-tabelas-inet.

## Fontes
- [MITRE Caldera Official GitHub — Automated Adversary Emulation, Red Team & Incident Response Platform](https://raw.githubusercontent.com/mitre/caldera/master/README.md) — repositório oficial do MITRE Caldera v5 cobrindo o Core C2 Server, interface VueJS Magma e ecossistema de plugins (`sandcat`, `stockpile`, `atomic`, `emu`, `debrief`, `response`); consultado em 2026-10-03.
- [MITRE Caldera Official Documentation — Learning the Terminology (`Agents`, `Abilities`, `Adversaries`, `Operations`, `Planners`, `Facts`, `Parsers`)](https://caldera.readthedocs.io/en/latest/Learning-the-terminology.html) — documentação oficial ReadTheDocs detalhando a arquitetura de planejamento orientado a fatos e agentes do Caldera; consultado em 2026-10-03.
