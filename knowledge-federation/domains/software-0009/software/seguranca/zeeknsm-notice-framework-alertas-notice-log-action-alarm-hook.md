---
id: software.seguranca.tranche03.000205
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-03.md"
fontes: ["https://raw.githubusercontent.com/zeek/zeek/master/doc/about/architecture.rst", "https://raw.githubusercontent.com/zeek/zeek/master/README.md", "https://github.com/zeek/zeek"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Zeek Notice Framework (`notice.log`): geração de alertas contextuais (`NOTICE`), deduplicação por `suppress_for` e hooks de resposta

## Em uma frase
Enquanto os logs normais do Zeek (`conn.log`, `dns.log`) são neutros de política, o **Notice Framework** é o subsistema pelo qual scripts do Zeek emitem alertas acionáveis quando detectam comportamentos anômalos ou violações de política, gravando-os em **`notice.log`** através da função **`NOTICE([$note=..., $msg=..., $conn=c, $identifier=..., $suppress_for=...])`**.

## Por que importa
Emitir milhares de alertas idênticos quando um host infectado tenta conectar-se a um servidor C2 a cada segundo inunda o SIEM; o Notice Framework resolve isso nativamente no próprio motor de script.

## Como funciona
Ao preencher os campos **`$identifier`** (uma string única que identifica a entidade, ex.: o par IP origem + destino) e **`$suppress_for=1hr`** na chamada `NOTICE(...)`, o Zeek suprime automaticamente alertas duplicados com o mesmo identificador em todo o cluster pelo período configurado, e permite rotear tipos críticos (`Notice::ACTION_ALARM`, `Notice::ACTION_EMAIL`) via `hook Notice::policy(n: Notice::Info)`!

## Exemplo
```zeek
# Emitindo um alerta estruturado no notice.log com supressão automática de duplicatas por 30 minutos:
redef enum Notice::Type += {
    Suspicious_User_Agent
};

event http_header(c: connection, is_orig: bool, original_name: string, name: string, value: string)
    {
    if ( is_orig && name == "USER-AGENT" && /curl|sqlmap|nikto/ in value )
        {
        NOTICE([
            $note=Suspicious_User_Agent,
            $msg=fmt("User-Agent de automação/scan detectado: %s", value),
            $conn=c,
            $identifier=cat(c$id$orig_h, value),
            $suppress_for=30mins
        ]);
        }
    }
```

## Limites e trade-offs
Use `hook Notice::policy(n: Notice::Info)` na configuração local (`local.zeek`) para elevar notas críticas para `ACTION_ALARM` ou ignorar avisos informativos de sub-redes de laboratório.

## Como verificar
Execute o script acima sobre um PCAP de teste e verifique a criação e os campos de `notice.log`.

## Conexões
- [[zeeknsm-file-analysis-framework-faf-extracao-arquivos-hashing-mime]] — Veja também: Zeek File Analysis Framework (`FAF`): dissecção agnóstica de protocolo, detecção de MIME (`file_sniff`) e cálculo de hashes (`MD5`, `SHA1`, `SHA256`).
- [[zeeknsm-intelligence-framework-ioc-matching-ips-domains-hashes-cif]] — Veja também: Zeek Intelligence Framework (`intel.log`): ingestão em tempo real de Indicadores de Comprometimento (`ADDR`, `DOMAIN`, `URL`, `FILE_HASH`, `CERT_HASH`).

## Fontes
- [Zeek GitHub — README.md (Network Traffic Analysis & Security Monitoring Framework, Key Features, Scripting & Tooling)](https://raw.githubusercontent.com/zeek/zeek/master/doc/about/architecture.rst) — README oficial do zeek/zeek apresentando o framework de análise semântica de rede, estado de camada de aplicação e linguagem de scripts; consultado em 2026-10-03.
- [Zeek Official Documentation — Architecture (doc/about/architecture.rst: Event Engine, Packet/Session/File Analysis & Script Interpreter)](https://raw.githubusercontent.com/zeek/zeek/master/README.md) — Documentação oficial de arquitetura do Zeek detalhando a separação entre o Event Engine neutro de política e o Script Interpreter; consultado em 2026-10-03.
- [Zeek Network Security Monitor — Official GitHub Repository](https://github.com/zeek/zeek) — Repositório oficial BSD-3-Clause do Zeek; consultado em 2026-10-03.
