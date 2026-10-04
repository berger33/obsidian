---
id: software.seguranca.tranche12.001128
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

# Emulação Automática de **Movimentação Lateral** no Caldera: Encadeando Descoberta de Sub-rede, Extração de Credenciais e Pivô SMB/SSH/WinRM

## Em uma frase
Como o Caldera consegue entrar em um único host inicial (*Patient Zero*) e se espalhar autonomamente para outros servidores da sub-rede de laboratório sem intervenção manual do operador?

## Por que importa
O segredo está no encadeamento de três famílias de *Abilities* através do banco de **Facts** da operação: **(1) Discovery & Credential Access** — o primeiro agente Sandcat executa comandos que descobrem hosts vizinhos (gerando fatos `remote.host.ip` / `remote.host.fqdn`) e extrai credenciais locais ou chaves SSH (gerando fatos `host.user.name`, `host.user.password`, `host.user.ntlm` ou `host.user.ssh_key`); **(2) Lateral Movement** — o Planner verifica que os requisitos (`remote.host.ip` + credencial) foram satisfeitos e instancia *Abilities* de cópia remota do binário do Sandcat (via `scp`, compartilhamento administrativo SMB `ADMIN$`/`C$` ou WinRM/WMI); e **(3) Remote Execution** — o novo agente Sandcat inicia no segundo host, faz check-in no servidor Caldera sob o mesmo grupo e entra imediatamente no loop da operação em andamento!

## Como funciona
Quando um segundo agente faz check-in durante uma operação ativa, o Planner do Caldera passa automaticamente a agendar as *Abilities* também nesse novo host, reproduzindo fielmente o efeito cascata de uma intrusão real!

## Exemplo
```bash
# Inspecionar via API REST v2 todos os Facts descobertos dinamicamente pelos agentes durante uma operacao no Caldera
CALDERA_API_KEY="ADMIN123"
curl -sS -H "KEY: ${CALDERA_API_KEY}" http://127.0.0.1:8888/api/v2/facts | \
  jq '[.found[] | {trait: .trait, value: .value, score: .score, collected_by: .collected_by}]'
```

## Limites e trade-offs
Para evitar que um exercício de movimentação lateral do Caldera escape da VLAN de laboratório e tente conectar em servidores de produção, configure **Regras de Fatos (*Fact Rules / Deny Rules*)** na *Fact Source* da operação restringindo o trait `remote.host.ip` exclusivamente ao CIDR da sub-rede de laboratório (ex.: permitir apenas `10.99.50.0/24`)!

## Como verificar
Essa trava de escopo via *Fact Rules* é obrigatória em qualquer exercício automatizado de movimentação lateral.

## Conexões
- [[caldera-relatorios-debrief-api-rest-automacao-cicd]] — Veja também: Automação via **API REST v2 (`/api/v2/operations`)** e Relatórios Executivos/Técnicos com o Plugin **`debrief`** do Caldera.
- [[caldera-hardening-seguranca-implantacao-ssl-local-yml-autenticacao]] — Veja também: Hardening e Segurança Operacional de uma Implantação do **MITRE Caldera**: `conf/local.yml`, Plugin **`ssl`**, **`saml`** e Isolamento de Rede.
- [[caldera-arquitetura-plataforma-emulacao-adversarios-c2-plugins]] — Referência cruzada direta com caldera-arquitetura-plataforma-emulacao-adversarios-c2-plugins.
- [[caldera-abilities-adversary-profiles-planners-facts-parsers]] — Referência cruzada direta com caldera-abilities-adversary-profiles-planners-facts-parsers.
- [[chainsaw-deteccao-movimentacao-lateral-logins-brute-force-contas]] — Referência cruzada direta com chainsaw-deteccao-movimentacao-lateral-logins-brute-force-contas.

## Fontes
- [MITRE Caldera Official GitHub — Automated Adversary Emulation, Red Team & Incident Response Platform](https://raw.githubusercontent.com/mitre/caldera/master/README.md) — repositório oficial do MITRE Caldera v5 cobrindo o Core C2 Server, interface VueJS Magma e ecossistema de plugins (`sandcat`, `stockpile`, `atomic`, `emu`, `debrief`, `response`); consultado em 2026-10-03.
- [MITRE Caldera Official Documentation — Learning the Terminology (`Agents`, `Abilities`, `Adversaries`, `Operations`, `Planners`, `Facts`, `Parsers`)](https://caldera.readthedocs.io/en/latest/Learning-the-terminology.html) — documentação oficial ReadTheDocs detalhando a arquitetura de planejamento orientado a fatos e agentes do Caldera; consultado em 2026-10-03.
